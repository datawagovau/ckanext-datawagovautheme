import sys
from datetime import datetime, timedelta

import ckan.plugins as p
import ckan.model as model
from ckan.common import config


class WaCommand(p.toolkit.CkanCommand):
    """
    The available commands are:

        clean-activity   - Remove old activity records for preconfigured users
    """

    summary = __doc__.split('\n')[0]
    usage = __doc__
    max_args = None
    min_args = 1

    def command(self):
        import logging
        self._load_config()
        self.log = logging.getLogger("ckan.lib.cli")

        cmd_name = self.args[0]
        cmd = getattr(self, '_' + cmd_name.replace('-', '_'), None)
        if not cmd:
            self.parser.error('Command not recognized: %r' % cmd_name)
        cmd(*self.args[1:])

    def _clean_activity(self):
        users = p.toolkit.aslist(config.get('ckanext.wa.cleanable_users'))
        max_age = p.toolkit.asint(
            config.get('ckanext.wa.max_activity_age_in_days', 30)
        )

        if not users:
            self.parser.error('`ckanext.wa.cleanable_users` is not defined')
        for name in users:
            self.log.info('Cleaning activity of %s', name)
            user = model.User.get(name)
            activities = model.Session.query(model.Activity.id).filter(
                model.Activity.user_id == user.id, model.Activity.timestamp <
                datetime.utcnow() - timedelta(days=max_age)
            )
            details = model.Session.query(model.ActivityDetail).filter(
                model.ActivityDetail.activity_id.in_(activities.subquery())
            )
            self.log.info(
                'Removed %s records from activity_detail table',
                details.delete(synchronize_session=False)
            )
            self.log.info(
                'Removed %s records from activity table',
                activities.delete(synchronize_session=False)
            )
            model.Session.commit()
