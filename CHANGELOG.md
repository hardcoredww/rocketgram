# Changelog
All notable changes to this project.


## [Unreleased]


## [2.0.1] - 2020-05-16

### Fixed
- Fixed bug in `ResponseParameters` response class.
- Fixed typing.


## [2.0] - 2020-05-02

### Added
- Added `callback` context helper.
- Added `shipping` context helper.
- Added `checkout` context helper.
- Added `poll` context helper.
- Added `answer` context helper.
- Added well typed `Request.send2()` method. This method returns result directly instead of `Response` object.
- Added well typed `Response.method` property.
- Added `File.url` property. This property retrun url of a file requested by `GetFile` method.
- Ability to use callable classes and instances as handlers.
- `explanation`, `explanation_entities`, `open_period`, `close_date` fields to `Poll` class.
- `explanation`, `explanation_parse_mode`, `open_period`, `close_date` fields to `sendPoll` request class.
- `emoji` field to `sendDice` request class.
- `emoji` field to `Dice` class.

### Fixed
- Minor bugfixes.

### Changed
- Refactored api.

### Removed
- Old `context` helper functions. Now `context` and `context2` is the same.

### Deprecated
- `context2` is deprecated and will be removed in version 2.3.
- `Request.send()` method is deprecated and will be removed in version 2.3. Use `Request.send2()` instead.
- `Response.method` property is deprecated and will be removed in version 2.3. Use `Response.request` instead.
- `BaseDispatcherProxy` class is deprecated and will be removed in version 3.0. Use `BaseDispatcher` instead.
- `BaseDispatcher.from_proxy` method is deprecated and will be removed in version 3.0. Use `from_dispatcher` instead.

### Changed
- Framework now corresponds to Telegram Bot API 4.8.


## [1.8] - 2020-04-11

### Added
- Added `SendDice` request class.
- Added `Dice` update class.
- Added `dice` field to `Message` class.
- Added `SetMyCommands` request class.
- Added `GetMyCommands` request class.
- Added `GetStickerSetThumb` request class.
- Added `tgs_sticker` field to `AddStickerToSet` request class.
- Added `tgs_sticker` and `thumb` fields to `StickerSet` request class.

### Changed
- Framework now corresponds to Telegram Bot API 4.7.


## [1.7] - 2020-02-29

### Added
- More typing.
- `language` field to `MessageEntity` class.
- New `PollType` class.
- `can_join_groups` field to `User` class.
- `can_read_all_group_messages` field to `User` class.
- `can_join_groups` field to `User` class.
- New `PollAnswer` class.
- New update type `poll_answer` in `UpdateType` class.
- `poll_answer` to `Update` class.
- `poll` method to `ReplyKeyboard` class.
- `is_anonymous` field to `SendPoll` request class.
- `type` field to `SendPoll` request class.
- `allows_multiple_answers` field to `SendPoll` request class.
- `correct_option_id` field to `SendPoll` request class.
- `is_closed` field to `SendPoll` request class.

### Fixed
- Bug when use middlewares.
- Bug in ChatMember object.
- `first_name` in `User` class now mandatory as expected.

### Changed
- Framework now corresponds to Telegram Bot API 4.6.


## [1.6.1] - 2020-01-04

### Fixed
- Import bug quickfix.


## [1.6] - 2020-01-04

### Added
- `Keyboard` object now can be passed to request without rendering.
- Support new entity types `underline` and `strikethrough`.
- Support parse mode type `markdownv2`.
- New `file_unique_id` field to various objects.
- New `small_file_unique_id` and `big_file_unique_id` to `ChatPhoto` object.
- New `custom_title` to `ChatMember` object.
- New `slow_mode_delay` to `Chat` object.
- New `setChatAdministratorCustomTitle` request object.
- Support nested entities.

### Fixed
- Fixed bug in webhook-reply in `TornadoExecutor`.

### Changed
- Framework now corresponds to Telegram Bot API 4.5.


## [1.5] - 2019-08-04

### Added
- `permissions` field to `RestrictChatMember` request object.
- `SetChatPermissions` request object.
- `permissions` field to `Chat` object.
- `can_send_polls` field to `ChatMember` object.
- `ChatPermissions` object.
- `is_animated` field to `Sticker` request object.

### Changed
- Framework now corresponds to Telegram Bot API 4.4.

### Removed
- `can_send_messages` field from `RestrictChatMember` request object.
- `can_send_media_messages` field from `RestrictChatMember` request object.
- `can_send_other_messages` field from `RestrictChatMember` request object.
- `can_add_web_page_previews` field from `RestrictChatMember` request object.
- `all_members_are_administrators` field from `Chat` request object.


## [1.4] - 2019-07-26

### Fixed
- Final fix optional module imports.
- Fix issue in message_type filter.
- Fix issue in Connector with the inability to send files with unicode names.


## [1.3] - 2019-07-13

### Added
- Added new context2 context helpers.

### Fixed
- Fix optional module imports.

### Deprecated
- Old context helpers is deprecated. It will be replaced with `context2` in version 2.0.


## [1.2] - 2019-06-01

### Added
- Added LoginUrl type.
- InlineKeyboardButton now accepts LoginUrl.
- Added login() method to InlineKeyboard.
- Added parse() to InlineKeyboardButton, LoginUrl InlineKeyboardMarkup.
- Added reply_markup field to Message.

### Changed
- Framework now corresponds to Telegram Bot API 4.3.


## [1.1] - 2019-05-31

### Added
- Start using "changelog".
- Added some tests.
- Added travis.
- Fixed types in types.py
- Fixed bug in EditMessageMedia.

### Changed
- context-helpers now have optional types.

### Fixed
- Fixed logger names in executor.py and aiohttp.py.
- Fixed waiters cleaner routine.
- Fixed MediaGroups's default values.


## [1.0] - 2019-04-26

### Added
- Released version 1.0.
