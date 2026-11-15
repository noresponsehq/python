from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


RecordKind = Union[
    Literal[
        # An email address. value: in lower case, without a mailto: prefix.
        "email",
        # A phone number. value: in E.164 form, such as +447700900123. A national number is cleaned only when the country of the source's site is known.
        "phone",
        # A handle a person chose. value: as written. Compare it in lower case. A value that is only zeros, or null, nil, none, undefined or n/a, has no value.
        "username",
        # A platform's own id for an account. value: as written. A value that is only zeros, or null, nil, none, undefined or n/a, has no value.
        "account_id",
        # A web address. value: the scheme and host in lower case, the path, query and fragment as written.
        "url",
        # A host name with no path. value: in lower case, also when the source wrote a URL.
        "domain",
        # A picture, as a link or a file. value: the link, cleaned as a `url`, else the file as written. A value that is only zeros, or null, nil, none, undefined or n/a, has no value.
        "image",
        # A whole name or a part of one. value: with each run of spaces made one space.
        "person_name",
        # A stated gender. value: `female`, `male` or `other` when the value names one of them, else as written.
        "gender",
        # An age in years. value: a whole number from 0 to 150.
        "age",
        # A language. value: its ISO 639 code, two letters when the language has them.
        "language",
        # A company, school or group by name. value: with each run of spaces made one space.
        "organisation",
        # A position or occupation. value: as written.
        "job_title",
        # A country. value: its ISO 3166-1 alpha-2 code, such as GB.
        "country",
        # A state, province or county. value: as written.
        "region",
        # A city or town. value: as written.
        "city",
        # A street address or one line of it. value: as written. A value that is only zeros, or null, nil, none, undefined or n/a, has no value.
        "address",
        # A postal code. value: in upper case with single spaces.
        "postcode",
        # A latitude and longitude. value: `latitude,longitude` in decimal degrees.
        "coordinates",
        # A timezone or an offset. value: an IANA zone name, UTC, or an offset such as +05:30.
        "timezone",
        # A calendar date. value: in ISO form at the precision the source gives: 2014, 2014-03 or 2014-03-07.
        "date",
        # A moment. value: in ISO form in UTC, such as 2014-03-07T09:30:00Z, or a date when the source gives no time.
        "date_time",
        # A length of time. value: a number of seconds.
        "duration",
        # An IPv4 or IPv6 address. value: its standard text form. An IPv4 address stored as a whole number is written as IPv4.
        "ip",
        # A network card address. value: in lower case with colons.
        "mac_address",
        # An id of a phone, computer or browser. value: as written. A value that is only zeros, or null, nil, none, undefined or n/a, has no value.
        "device_id",
        # A browser or app signature. value: as written.
        "user_agent",
        # A password in plain text. value: exactly as written, spaces included.
        "password",
        # A password hash. value: as written. detail names the likely algorithm, such as bcrypt.
        "hash",
        # The salt for a hash. value: exactly as written.
        "salt",
        # A session, reset or API token. value: as written. A value that is only zeros, or null, nil, none, undefined or n/a, has no value.
        "token",
        # A security question or its answer. value: exactly as written.
        "security_answer",
        # A payment card number. value: its 12 to 19 digits only.
        "card_number",
        # An IBAN or account number. value: its letters and digits only, in upper case.
        "bank_account",
        # A wallet address. value: as written. detail names the likely coin, such as BTC.
        "crypto_address",
        # Money, with its currency when given. value: a plain decimal. detail names the currency, such as USD.
        "amount",
        # A passport, tax, national or licence number. value: as written. A value that is only zeros, or null, nil, none, undefined or n/a, has no value.
        "id_number",
        # A number plate or a VIN. value: in upper case with no spaces.
        "vehicle",
        # One of a small set, such as a status or level. value: as written.
        "label",
        # Free writing, such as a bio or signature. value: as written.
        "long_text",
        # A whole number of things. value: a whole number of 0 or more, with no thousands separators.
        "count",
        # A rating, rank or points. value: a plain decimal.
        "score",
        # A yes or no. value: `true` or `false`.
        "flag",
        # A nested value that could not be split. value: as written.
        "structured",
        # Anything else. value: as written.
        "text",
    ],
    UnrecognizedStr,
]
r"""What sort of value a field holds, which decides how it is cleaned, compared and searched again. It comes from the value itself where its shape is certain (an email, an IP, a URL, an international phone number), else from the answer stored for the source's column, else text. A value of any kind is returned. Each kind's description says what it holds and the form value takes."""
