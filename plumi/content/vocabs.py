from zope.i18nmessageid import MessageFactory
_ = MessageFactory("plumi")

vocab_set = {}

taxonomy_sub_folder={'topic':'video_categories','genre':'video_genre','callouts':'submission_categories','countries':'video_countries'}

vocab_set['video_countries'] = (
         ('none', _(u'----------------')),
         ('XX', _('-- International --')),
        )

vocab_set['video_categories'] = (
        )
vocab_set['video_genre'] = (
         ('none', _(u'----------------')),
        )
vocab_set['submission_categories'] = (
         ('none', _(u'----------------')),
        ) 

