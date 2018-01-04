from errbot import BotPlugin, botcmd, arg_botcmd, webhook


class Deploy(BotPlugin):
    """
    Bot Plugin to deploy web apps
    """

    # Passing split_args_with=None will cause arguments to be split on any kind
    # of whitespace, just like Python's split() does
    @botcmd(split_args_with=None)
    def deploy_reviews(self, message, args):
        output = 'Unable to process!'
        if len(args) < 1:
            return 'Not enough arguments. Try !supervisor help'

        additional = ' '.join(args) if args else ''
        output = run_cmd('bash /home/admin/ReviewProcessing/nonsvn/ansible/rerun_supervisor_program_on_production.sh {additional_params}'.format(additional_params=additional))
        return output

    @botcmd(split_args_with=None)
    def deploy_deep(self, message, args):
        output = 'Unable to process!'
        if len(args) < 1:
            return 'Not enough arguments. Try !supervisor help'

        additional = ' '.join(args) if args else ''
        output = run_cmd('bash /home/admin/Deep/nonsvn/ansible/rerun_supervisor_program_on_production.sh {additional_params}'.format(additional_params=additional))
        return output

    @botcmd(split_args_with=None)
    def logs(self, message, args):
        additional = ' '.join(args) if args else ''
        output = run_cmd('tail /home/admin/logs/gunicorn_access.log /home/admin/logs/gunicorn_error.log {additional_params}'.format(additional_params=additional))
        return output


def run_cmd(cmd):
    import subprocess
    try:
        output = subprocess.check_output(
            cmd.split(),
            stderr=subprocess.STDOUT
        )
        if len(output) > 0:
            return output.decode()
        else:
            return "OK\n"
    except subprocess.CalledProcessError as err:
        if len(err.output):
            return err.output.decode()
        else:
            return "Error"

