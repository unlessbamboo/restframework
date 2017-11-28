# coding:utf8
'''
    User账户相关错误码, 描述格式:
        CODE_动作_对象_结果
        CODE_状态_对象
'''

CODE_UNEXIST_USER = 41001
CODE_UNEXIST_USER_MSG = u'用户不存在'

CODE_EXISTED_USER = 41002
CODE_EXISTED_USER_MSG = u'用户已存在'

CODE_UNEXIST_EMAIL = 41003
CODE_UNEXIST_EMAIL_MSG = u'邮箱不存在'

CODE_EXISTED_EMAIL = 41004
CODE_EXISTED_EMAIL_MSG = u'邮箱已存在'

CODE_BAD_AVATAR = 41005
CODE_BAD_AVATAR_MSG = u'无效的头像'

CODE_CHECK_PASSWD_FAILED = 41006
CODE_CHECK_PASSWD_FAILED_MSG = u'密码错误'

CODE_CHECK_CODE_FAILED = 41007
CODE_CHECK_CODE_FAILED_MSG = u'验证码错误'

CODE_MODIFY_USER_LIMIT = 41008
CODE_MODIFY_USER_LIMIT_MSG = u'更改用户超过限制'

CODE_UNACTIVATED_USER = 41009
CODE_UNACTIVATED_USER_MSG = u'已锁定的用户'


# Child and Parent
CODE_UNEXIST_CHILD = 41104
CODE_UNEXIST_CHILD_MSG = u'该下级没有上级信息'

CODE_UNEXIST_PARENT = 41105
CODE_UNEXIST_PARENT_MSG = u'该下级对应的上级不存在'

CODE_UNEXIST_CHILD_AND_PARENT = 41106
CODE_UNEXIST_CHILD_AND_PARENT_MSG = u'不存在上级和下级'

CODE_BIND_PARENT_FAILED = 41107
CODE_BIND_PARENT_FAILED_MSG = u'绑定上级失败'

CODE_EXISTED_PARENT = 41108
CODE_EXISTED_PARENT_MSG = u'已存在上级'


# country
CODE_UNEXIST_COUNTRY = 41201
CODE_UNEXIST_COUNTRY_MSG = u'国家不存在'

CODE_EXISTED_COUNTRY = 41202
CODE_EXISTED_COUNTRY_MSG = u'国家经存在'

CODE_UNEXIST_LOCALE = 41203
CODE_UNEXIST_LOCALE_MSG = u'语言不存在'

CODE_EXISTED_LOCALE = 41204
CODE_EXISTED_LOCALE_MSG = u'语言已经存在'

CODE_UNEXIST_TESTIMONIAL = 41205
CODE_UNEXIST_TESTIMONIAL_MSG = u'用户证言不存在'