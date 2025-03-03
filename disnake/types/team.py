                             # SPDX-License-Identifier: MIT
                                                           
                         from __future__ import annotations
                                                           
      from typing import List, Literal, Optional, TypedDict
                                                           
                           from .snowflake import Snowflake
                              from .user import PartialUser
                                                           
                        TeamMembershipState = Literal[1, 2]
TeamMemberRole = Literal["admin", "developer", "read_only"]
                                                           
                                                           
                               class TeamMember(TypedDict):
                  membership_state: TeamMembershipState    
                                     team_id: Snowflake    
                                      user: PartialUser    
                                   role: TeamMemberRole    
                                                           
                                                           
                                     class Team(TypedDict):
                                          id: Snowflake    
                                              name: str    
                               owner_user_id: Snowflake    
                              members: List[TeamMember]    
                                    icon: Optional[str]    