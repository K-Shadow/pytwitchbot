from modules.cmds.cmdmodule import *


# Module to display help information for a specified command. ###


class CmdModuleHelp(CmdModule):
    def __init__(self, log, irc):
        super().__init__(log, irc)
        self.mod_type = 'all'
        self.cmd_dict = {'help': {'function': self.help_cmd, 'help':
                         'help <command> - Shows help for a specified command.'}}

    def help_cmd(self, userinfo, dest, args):
        if len(args) > 1 and args[1] != '':
            if args[1] in self.irc.modhandler.commands:
                self.irc.msg(dest, self.irc.modhandler.get_help_text(args[1], "chan"))
            elif args[1] in self.irc.modhandler.privcmds and not dest.startswith('#'):
                self.irc.msg(dest, self.irc.modhandler.get_help_text(args[1], "priv"))
            elif args[1] == "all":
                cmdlist = ""
                if dest.startswith('#'):
                    for cmd in self.irc.modhandler.commands:
                        cmdlist = cmdlist + cmd + " "
                    self.irc.msg(dest, "Bot command list (for channels): %s" % cmdlist)
                    self.irc.msg(dest, 'To view the list of commands available for use in private messages, '
                                       'whisper "!help all" to me directly.')
                else:
                    for cmd in self.irc.modhandler.privcmds:
                        cmdlist = cmdlist + cmd + " "
                    self.irc.msg(dest, "Bot command list (for private messages): %s" % cmdlist)
                    self.irc.msg(dest, 'To view the list of commands available for use in channels, '
                                       'send "!help all" in any channel I\'m in.')
            else:
                self.irc.msg(dest, 'Help for that command wasn\'t found.')
        else:
            self.irc.msg(dest, self.irc.modhandler.get_help_text(self.irc.cmd_prefix + 'help', self.mod_type))

