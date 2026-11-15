from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


RecordRole = Union[
    Literal[
        # The platform's own id for the account (`account_id`).
        "account_id",
        # The state of the account, such as active or suspended (`label`).
        "account_status",
        # The sort of account, such as personal or business (`label`).
        "account_type",
        # A mobile, alternate or fax number beside the main one (`phone`).
        "alternate_phone",
        # Money held on the account (`amount`).
        "balance",
        # Whether the site banned the account (`flag`).
        "banned",
        # What the person wrote about themselves (`long_text`).
        "bio",
        # The date of birth (`date` or `date_time`).
        "born",
        # Whether the site marks the account as a bot (`flag`).
        "bot",
        # The category callers give a phone number, such as telemarketer (`label`).
        "caller_category",
        # How many chargebacks a shop recorded against the account, or whether it has one (`count` or `flag`).
        "chargebacks",
        # Another account on the same platform the account deals with, such as an opponent it plays most or a follower (`username`). Fields beside it under the same name say how, how often and when last. It names another person, never the account's owner.
        "contact",
        # The banner picture of the profile (`image`).
        "cover_picture",
        # How many of the account's payments a shop declined (`count`).
        "declines",
        # Whether the account is deleted or inactive (`flag`).
        "deleted",
        # When the account was deleted (`date` or `date_time`).
        "deleted_on",
        # A department the source names (`text`).
        "department",
        # The name the account shows (`person_name`).
        "display_name",
        # Whether the site verified the email (`flag`).
        "email_verified",
        # When the account or its subscription expires (`date` or `date_time`).
        "expires",
        # A first name (`person_name`).
        "first_name",
        # How many accounts follow the account (`count`).
        "followers",
        # How many accounts the account follows (`count`).
        "following",
        # How many friends the account has (`count`).
        "friends",
        # A whole postal address on one line (`address`).
        "full_address",
        # A whole name (`person_name`).
        "full_name",
        # The handle of the account (`username`).
        "handle",
        # A headline or user title shown with the name (`text`).
        "headline",
        # Interests the person lists (`text`).
        "interests",
        # A job title the source states (`job_title`).
        "job_title",
        # When the account was made (`date` or `date_time`).
        "joined",
        # When the account was last active (`date` or `date_time`).
        "last_active",
        # The IP the account last used (`ip`).
        "last_ip",
        # A last name (`person_name`).
        "last_name",
        # When the account last posted (`date` or `date_time`).
        "last_post",
        # When the account or its profile last changed (`date` or `date_time`).
        "last_updated",
        # A level or rank on the site (`label`).
        "level",
        # How many likes the account gave (`count`).
        "likes_given",
        # How many likes the account received (`count`).
        "likes_received",
        # The line type of a phone number, such as mobile or VoIP (`label`).
        "line_type",
        # An account on another network. The field's name names the network (`username`, `account_id` or `url`).
        "linked_account",
        # A place as the person wrote it (`text`).
        "location",
        # Whether callers mark a phone number as spam (`flag`).
        "marked_spam",
        # A middle name (`person_name`).
        "middle_name",
        # A nationality (`country`).
        "nationality",
        # An organisation the source names, such as a company (`organisation`).
        "organisation",
        # An IP whose use the source does not say (`ip`).
        "other_ip",
        # Whether the account is paid or premium (`flag`).
        "paid",
        # When the password last changed (`date` or `date_time`).
        "password_changed",
        # The payment method or card brand the account paid with (`label`).
        "payment_method",
        # The profile picture (`image`).
        "picture",
        # Points on the site (`score`).
        "points",
        # How many posts the account made (`count`).
        "posts",
        # Whether the account is private (`flag`).
        "private",
        # The link to the profile (`url`).
        "profile_link",
        # How many times people viewed the profile (`count`).
        "profile_views",
        # A rating of the account (`score`).
        "rating",
        # How many people the account referred (`count`).
        "referrals",
        # Who or what referred the account (`text`).
        "referrer",
        # How many reports callers made on a phone number (`count`).
        "report_count",
        # Reputation on the site (`score`).
        "reputation",
        # A reputation label for a phone number (`label`).
        "reputation_label",
        # The country the person lives in (`country`).
        "residence",
        # A salutation or suffix, such as Dr or Jr (`text`).
        "salutation",
        # A school the source names (`organisation`).
        "school",
        # A signature the person posts under (`long_text`).
        "signature",
        # The IP the account was made from (`ip`).
        "signup_ip",
        # A role on the site, such as admin or moderator (`label`).
        "site_role",
        # How likely a phone number is spam, as the source scores it (`score`).
        "spam_score",
        # A street line of an address (`address`).
        "street",
        # How many trades a forum account completed (`count`).
        "trades",
        # Whether the site verified the account (`flag`).
        "verified",
        # Warnings and infractions on the account (`count`).
        "warnings",
        # A website the person lists (`url`).
        "website",
    ],
    UnrecognizedStr,
]
r"""Which common field a value is, where many sources share it: a join date and a birth date are both dates, with the roles joined and born. A platform account's field and a breach row's column with the same meaning carry the same kind and role. A linked_account field is named by its network. Absent for a field only its source returns. Each role's description names the kinds its values have."""
