from typing import Any, Callable, List, Optional, Tuple, TypeVar
from joint_teapot.workers.gitea import Gitea,PermissionEnum,list_all,first
from joint_teapot.utils.logger import logger
from joint_teapot.config import settings
from focs_gitea.rest import ApiException
def create_teams_and_repos(
    gitea:Gitea,
    group: str,
    usernames: List[str],
    template: str = "",
    permission: PermissionEnum = PermissionEnum.write,
) -> bool:
    teams = list_all(gitea.organization_api.org_list_teams, gitea.org_name)
    repos = list_all(gitea.organization_api.org_list_repos, gitea.org_name)
    team_name = group
    repo_name = group
    if team_name is None or repo_name is None:
        return False
    team = first(teams, lambda team: team.name == team_name)
    if team is None:
        team = gitea.organization_api.org_create_team(
            gitea.org_name,
            body={
                "can_create_org_repo": False,
                "includes_all_repositories": False,
                "name": team_name,
                "permission": permission.value,
                "units": [
                    "repo.code",
                    "repo.issues",
                    "repo.ext_issues",
                    "repo.wiki",
                    "repo.pulls",
                    "repo.releases",
                    "repo.projects",
                    "repo.ext_wiki",
                ],
            },
        )
        logger.info(f"Team {team_name} created")
    else:
        logger.info(f"Team {team_name} already exists")
    if first(repos, lambda repo: repo.name == repo_name) is None:
        if template == "":
            gitea.organization_api.create_org_repo(
                gitea.org_name,
                body={
                    "auto_init": False,
                    "default_branch": settings.default_branch,
                    "name": repo_name,
                    "private": True,
                    "template": False,
                    "trust_model": "default",
                },
            )
        else:
            gitea.repository_api.generate_repo(
                gitea.org_name,
                template,
                body={
                    "default_branch": settings.default_branch,
                    "git_content": True,
                    "git_hooks": True,
                    "labels": True,
                    "name": repo_name,
                    "owner": gitea.org_name,
                    "private": True,
                    "protected_branch": True,
                },
            )
        logger.info(f"{gitea.org_name}/{repo_name} created")
    else:
        logger.info(f"Repository {gitea.org_name}/{repo_name} already exists")
    try:
        gitea.organization_api.org_add_team_repository(
            team.id, gitea.org_name, repo_name
        )
    except Exception as e:
        logger.warning(e)
    for username in usernames:
        try:
            gitea.organization_api.org_add_team_member(team.id, username)
            gitea.repository_api.repo_add_collaborator(
                gitea.org_name, repo_name, username
            )
        except Exception as e:
            logger.error(e)
            continue
    try:
        gitea.repository_api.repo_delete_branch_protection(
            gitea.org_name, repo_name, settings.default_branch
        )
    except ApiException as e:
        if e.status != 404:
            raise
    # no branch protection needed
    # try:
    #     gitea.repository_api.repo_create_branch_protection(
    #         gitea.org_name,
    #         repo_name,
    #         body={
    #             "block_on_official_review_requests": True,
    #             "block_on_outdated_branch": True,
    #             "block_on_rejected_reviews": True,
    #             "branch_name": settings.default_branch,
    #             "dismiss_stale_approvals": True,
    #             "enable_approvals_whitelist": False,
    #             "enable_merge_whitelist": False,
    #             "enable_push": True,
    #             "enable_push_whitelist": True,
    #             "merge_whitelist_teams": [],
    #             "merge_whitelist_usernames": [],
    #             "protected_file_patterns": "",
    #             "push_whitelist_deploy_keys": False,
    #             "push_whitelist_teams": ["Owners"],
    #             "push_whitelist_usernames": [],
    #             "require_signed_commits": False,
    #             "required_approvals": 0,
    #             "enable_status_check": True,
    #         },
    #     )
    # except ApiException as e:
    #     if e.status != 404:
    #         raise
    logger.info(f"{gitea.org_name}/{repo_name} jobs done")
    return True