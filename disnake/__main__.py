                                                                              # SPDX-License-Identifier: MIT
                                                                                                            
                                                                                             import argparse
                                                                                   import importlib.metadata
                                                                                             import platform
                                                                                                  import sys
                                                                                    from pathlib import Path
                                                                                    from typing import Union
                                                                                                            
                                                                                              import aiohttp
                                                                                                            
                                                                                              import disnake
                                                                                                            
                                                                                                            
                                                                                 def show_version() -> None:
                                                                                            entries = []    
                                                                                                            
                                                                              sys_ver = sys.version_info    
                                                                                         entries.append(    
                 f"- Python v{sys_ver.major}.{sys_ver.minor}.{sys_ver.micro}-{sys_ver.releaselevel}"        
                                                                                                       )    
                                                                      disnake_ver = disnake.version_info    
                                                                                         entries.append(    
f"- disnake v{disnake_ver.major}.{disnake_ver.minor}.{disnake_ver.micro}-{disnake_ver.releaselevel}"        
                                                                                                       )    
                                                                                                    try:    
                                                     version = importlib.metadata.version("disnake")        
                                                         except importlib.metadata.PackageNotFoundError:    
                                                                                                pass        
                                                                                                   else:    
                                     entries.append(f"    - disnake importlib.metadata: v{version}")        
                                                                                                            
                                                     entries.append(f"- aiohttp v{aiohttp.__version__}")    
                                                                                uname = platform.uname()    
        entries.append(f"- system info: {uname.system} {uname.release} {uname.version} {uname.machine}")    
                                                                               print("\n".join(entries))    
                                                                                                            
                                                                                                            
                                                    def core(parser: argparse.ArgumentParser, args) -> None:
                                                     # this method runs when no subcommands are provided    
                                                     # as such, we can assume that we want to print help    
                                                                                        if args.version:    
                                                                                      show_version()        
                                                                                                   else:    
                                                                                 parser.print_help()        
                                                                                                            
                                                                                                            
                                                    _interaction_bot_init = """super().__init__(**kwargs)"""
                                                                                      _commands_bot_init = (
                     'super().__init__(command_prefix=commands.when_mentioned_or("{prefix}"), **kwargs)'    
                                                                                                           )
                                                                   _bot_template = """#!/usr/bin/env python3
                                                                                                            
                                                                            from disnake.ext import commands
                                                                                              import disnake
                                                                                               import config
                                                                                                            
                                                                                                            
                                                                                 class Bot(commands.{base}):
                                                                           def __init__(self, **kwargs):    
                                                                                              {init}        
                                                                             for cog in config.cogs:        
                                                                                            try:            
                                                                    self.load_extension(cog)                
                                                                        except Exception as exc:            
       print(f"Could not load extension {{cog}} due to {{exc.__class__.__name__}}: {{exc}}")                
                                                                                                            
                                                                               async def on_ready(self):    
                                         print(f"Logged on as {{self.user}} (ID: {{self.user.id}})")        
                                                                                                            
                                                                                                            
                                                                                                 bot = Bot()
                                                                                                            
                                                                               # write general commands here
                                                                                                            
                                                                                  if __name__ == "__main__":
                                                                                   bot.run(config.token)    
                                                                                                         """
                                                                                                            
                                            _gitignore_template = """# Byte-compiled / optimized / DLL files
                                                                                                __pycache__/
                                                                                                   *.py[cod]
                                                                                                  *$py.class
                                                                                                            
                                                                                              # C extensions
                                                                                                        *.so
                                                                                                            
                                                                                  # Distribution / packaging
                                                                                                     .Python
                                                                                                        env/
                                                                                                      build/
                                                                                               develop-eggs/
                                                                                                       dist/
                                                                                                  downloads/
                                                                                                       eggs/
                                                                                                      .eggs/
                                                                                                        lib/
                                                                                                      lib64/
                                                                                                      parts/
                                                                                                      sdist/
                                                                                                        var/
                                                                                                 *.egg-info/
                                                                                              .installed.cfg
                                                                                                       *.egg
                                                                                                            
                                                                                   # Our configuration files
                                                                                                   config.py
                                                                                                         """
                                                                                                            
                                                         _cog_template = '''from disnake.ext import commands
                                                                                              import disnake
                                                                                                            
                                                                          class {name}(commands.Cog{attrs}):
                                                             """The description for {name} goes here."""    
                                                                                                            
                                                                                def __init__(self, bot):    
                                                                                      self.bot = bot        
                                                                                                     {extra}
                                                                                             def setup(bot):
                                                                                bot.add_cog({name}(bot))    
                                                                                                         '''
                                                                                                            
                                                       # everything that is a _cog_special_method goes here.
                                                                                           _cog_extras = """
                                                                               async def cog_load(self):    
                                                                   # (async) loading logic goes here        
                                                                                                pass        
                                                                                                            
                                                                                   def cog_unload(self):    
                                                                          # clean up logic goes here        
                                                                                                pass        
                                                                                                            
                                                                                 ### Prefix Commands ###    
                                                                                                            
                                                                         async def cog_check(self, ctx):    
                                                 # checks that apply to every prefix command in here        
                                                                                         return True        
                                                                                                            
                                                                         async def bot_check(self, ctx):    
                                              # checks that apply to every prefix command to the bot        
                                                                                         return True        
                                                                                                            
                                                                    async def bot_check_once(self, ctx):    
                 # check that apply to every prefix command but is guaranteed to be called only once        
                                                                                         return True        
                                                                                                            
                                                          async def cog_command_error(self, ctx, error):    
                                                    # error handling to every prefix command in here        
                                                                                                pass        
                                                                                                            
                                                                 async def cog_before_invoke(self, ctx):    
                                                     # called before a prefix command is called here        
                                                                                                pass        
                                                                                                            
                                                                  async def cog_after_invoke(self, ctx):    
                                                      # called after a prefix command is called here        
                                                                                                pass        
                                                                                                            
                                                                                  ### Slash Commands ###    
                                                                                                            
                         # These are similar to the ones in the previous section, but for slash commands    
                                                                                                            
                                                         async def cog_slash_command_check(self, inter):    
                                                                                         return True        
                                                                                                            
                                                         async def bot_slash_command_check(self, inter):    
                                                                                         return True        
                                                                                                            
                                                    async def bot_slash_command_check_once(self, inter):    
                                                                                         return True        
                                                                                                            
                                                  async def cog_slash_command_error(self, inter, error):    
                                                                                                 ...        
                                                                                                            
                                                 async def cog_before_slash_command_invoke(self, inter):    
                                                                                                 ...        
                                                                                                            
                                                  async def cog_after_slash_command_invoke(self, inter):    
                                                                                                 ...        
                                                                                                            
                                                                 ### Message (Context Menu) Commands ###    
                                                                                                            
                                                       async def cog_message_command_check(self, inter):    
                                                                                         return True        
                                                                                                            
                                                       async def bot_message_command_check(self, inter):    
                                                                                         return True        
                                                                                                            
                                                  async def bot_message_command_check_once(self, inter):    
                                                                                         return True        
                                                                                                            
                                                async def cog_message_command_error(self, inter, error):    
                                                                                                 ...        
                                                                                                            
                                               async def cog_before_message_command_invoke(self, inter):    
                                                                                                 ...        
                                                                                                            
                                                async def cog_after_message_command_invoke(self, inter):    
                                                                                                 ...        
                                                                                                            
                                                                    ### User (Context Menu) Commands ###    
                                                                                                            
                                                          async def cog_user_command_check(self, inter):    
                                                                                         return True        
                                                                                                            
                                                          async def bot_user_command_check(self, inter):    
                                                                                         return True        
                                                                                                            
                                                     async def bot_user_command_check_once(self, inter):    
                                                                                         return True        
                                                                                                            
                                                   async def cog_user_command_error(self, inter, error):    
                                                                                                 ...        
                                                                                                            
                                                  async def cog_before_user_command_invoke(self, inter):    
                                                                                                 ...        
                                                                                                            
                                                   async def cog_after_user_command_invoke(self, inter):    
                                                                                                 ...        
                                                                                                         """
                                                                                                            
                                                                                                            
                                                      # certain file names and directory names are forbidden
                  # see: https://msdn.microsoft.com/en-us/library/windows/desktop/aa365247%28v=vs.85%29.aspx
                              # although some of this doesn't apply to Linux, we might as well be consistent
                                                                _ascii_table = dict.fromkeys('<>:"|?*', "-")
                                                                                                            
                                                                           # NUL (0) and 1-31 are disallowed
                                                            _byte_table = dict.fromkeys(map(chr, range(32)))
                                                               _base_table = {**_ascii_table, **_byte_table}
                                                                                                            
                                                             _translation_table = str.maketrans(_base_table)
                                                                                                            
                                                                                                            
                               def to_path(parser, name: Union[str, Path], *, replace_spaces: bool = False):
                                                                              if isinstance(name, Path):    
                                                                                         return name        
                                                                                                            
                                                                             if sys.platform == "win32":    
                                                                                       forbidden = (        
                                                                                          "CON",            
                                                                                          "PRN",            
                                                                                          "AUX",            
                                                                                          "NUL",            
                                                                                         "COM1",            
                                                                                         "COM2",            
                                                                                         "COM3",            
                                                                                         "COM4",            
                                                                                         "COM5",            
                                                                                         "COM6",            
                                                                                         "COM7",            
                                                                                         "COM8",            
                                                                                         "COM9",            
                                                                                         "LPT1",            
                                                                                         "LPT2",            
                                                                                         "LPT3",            
                                                                                         "LPT4",            
                                                                                         "LPT5",            
                                                                                         "LPT6",            
                                                                                         "LPT7",            
                                                                                         "LPT8",            
                                                                                         "LPT9",            
                                                                                                   )        
                                                    if len(name) <= 4 and name.upper() in forbidden:        
                               parser.error("invalid directory name given, use a different one")            
                                                                                                            
                                                               name = name.translate(_translation_table)    
                                                                                      if replace_spaces:    
                                                                       name = name.replace(" ", "-")        
                                                                                       return Path(name)    
                                                                                                            
                                                                                                            
                                                                           def newbot(parser, args) -> None:
                            new_directory = to_path(parser, args.directory) / to_path(parser, args.name)    
                                                                                                            
                                                    # as a note exist_ok for Path is a 3.5+ only feature    
                                                        # since we already checked above that we're >3.5    
                                                                                                    try:    
                                                    new_directory.mkdir(exist_ok=True, parents=True)        
                                                                                  except OSError as exc:    
                                         parser.error(f"could not create our bot directory ({exc})")        
                                                                                                            
                                                                           cogs = new_directory / "cogs"    
                                                                                                            
                                                                                                    try:    
                                                                           cogs.mkdir(exist_ok=True)        
                                                                         init = cogs / "__init__.py"        
                                                                                        init.touch()        
                                                                                  except OSError as exc:    
                                          print(f"warning: could not create cogs directory ({exc})")        
                                                                                                            
                                                                                                    try:    
                           with open(str(new_directory / "config.py"), "w", encoding="utf-8") as fp:        
                                        fp.write('token = "place your token here"\ncogs = []\n')            
                                                                                  except OSError as exc:    
                                               parser.error(f"could not create config file ({exc})")        
                                                                                                            
                                                                                                    try:    
                              with open(str(new_directory / "bot.py"), "w", encoding="utf-8") as fp:        
                                                                     if args.interaction_client:            
                                                                init = _interaction_bot_init                
                    base = "AutoShardedInteractionBot" if args.sharded else "InteractionBot"                
                                                                                           else:            
                                        init = _commands_bot_init.format(prefix=args.prefix)                
                                          base = "AutoShardedBot" if args.sharded else "Bot"                
                                            fp.write(_bot_template.format(base=base, init=init))            
                                                                                  except OSError as exc:    
                                                  parser.error(f"could not create bot file ({exc})")        
                                                                                                            
                                                                                     if not args.no_git:    
                                                                                                try:        
                      with open(str(new_directory / ".gitignore"), "w", encoding="utf-8") as fp:            
                                                               fp.write(_gitignore_template)                
                                                                              except OSError as exc:        
                                     print(f"warning: could not create .gitignore file ({exc})")            
                                                                                                            
                                                        print("successfully made bot at", new_directory)    
                                                                                                            
                                                                                                            
                                                                           def newcog(parser, args) -> None:
                                                               cog_dir = to_path(parser, args.directory)    
                                                                                                    try:    
                                                                        cog_dir.mkdir(exist_ok=True)        
                                                                                  except OSError as exc:    
                                          print(f"warning: could not create cogs directory ({exc})")        
                                                                                                            
                                                        directory = cog_dir / to_path(parser, args.name)    
                                                                directory = directory.with_suffix(".py")    
                                                                                                    try:    
                                             with open(str(directory), "w", encoding="utf-8") as fp:        
                                                                                      attrs = ""            
                                                        extra = _cog_extras if args.full else ""            
                                                                             if args.class_name:            
                                                                      name = args.class_name                
                                                                                           else:            
                                                                  name = str(directory.stem)                
                                                              if "-" in name or "_" in name:                
                                                 translation = str.maketrans("-_", "  ")                    
                             name = name.translate(translation).title().replace(" ", "")                    
                                                                                       else:                
                                                                     name = name.title()                    
                                                                                                            
                                                                           if args.display_name:            
                                                    attrs += f', name="{args.display_name}"'                
                                                                          if args.hide_commands:            
                                                attrs += ", command_attrs=dict(hidden=True)"                
                             fp.write(_cog_template.format(name=name, extra=extra, attrs=attrs))            
                                                                                  except OSError as exc:    
                                                  parser.error(f"could not create cog file ({exc})")        
                                                                                                   else:    
                                                        print("successfully made cog at", directory)        
                                                                                                            
                                                                                                            
                                                                     def add_newbot_args(subparser) -> None:
                   parser = subparser.add_parser("newbot", help="creates a command bot project quickly")    
                                                                        parser.set_defaults(func=newbot)    
                                                                                                            
                                                parser.add_argument("name", help="the bot project name")    
                                                                                    parser.add_argument(    
        "directory", help="the directory to place it in (default: .)", nargs="?", default=Path.cwd()        
                                                                                                       )    
                                                                                                            
                                                           group = parser.add_mutually_exclusive_group()    
                                                                                     group.add_argument(    
                     "--prefix", help="the bot prefix (default: $)", default="$", metavar="<prefix>"        
                                                                                                       )    
                                                                                     group.add_argument(    
                                                                              "--app-commands-only",        
                                                help="whether to only process application commands",        
                                                                                action="store_true",        
                                                                          dest="interaction_client",        
                                                                                                       )    
                                                                                    parser.add_argument(    
                "--sharded", help="whether to use an automatically sharded bot", action="store_true"        
                                                                                                       )    
                                                                                    parser.add_argument(    
              "--no-git", help="do not create a .gitignore file", action="store_true", dest="no_git"        
                                                                                                       )    
                                                                                                            
                                                                                                            
                                                                     def add_newcog_args(subparser) -> None:
                      parser = subparser.add_parser("newcog", help="creates a new cog template quickly")    
                                                                        parser.set_defaults(func=newcog)    
                                                                                                            
                                                        parser.add_argument("name", help="the cog name")    
                                                                                    parser.add_argument(    
                                                                                        "directory",        
                                                help="the directory to place it in (default: cogs)",        
                                                                                          nargs="?",        
                                                                               default=Path("cogs"),        
                                                                                                       )    
                                                                                    parser.add_argument(    
               "--class-name", help="the class name of the cog (default: <name>)", dest="class_name"        
                                                                                                       )    
                            parser.add_argument("--display-name", help="the cog name (default: <name>)")    
                                                                                    parser.add_argument(    
              "--hide-commands", help="whether to hide all commands in the cog", action="store_true"        
                                                                                                       )    
              parser.add_argument("--full", help="add all special methods as well", action="store_true")    
                                                                                                            
                                                                                                            
                                                                                           def parse_args():
          parser = argparse.ArgumentParser(prog="disnake", description="Tools for helping with disnake")    
           parser.add_argument("-v", "--version", action="store_true", help="shows the library version")    
                                                                          parser.set_defaults(func=core)    
                                                                                                            
                               subparser = parser.add_subparsers(dest="subcommand", title="subcommands")    
                                                                              add_newbot_args(subparser)    
                                                                              add_newcog_args(subparser)    
                                                                      return parser, parser.parse_args()    
                                                                                                            
                                                                                                            
                                                                                         def main() -> None:
                                                                             parser, args = parse_args()    
                                                                                 args.func(parser, args)    
                                                                                                            
                                                                                                            
                                                                                  if __name__ == "__main__":
                                                                                                  main()    