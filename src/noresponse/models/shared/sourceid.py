from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


SourceID = Union[
    Literal[
        "github",
        "phone",
        "breach",
        "rdap",
        "mx",
        "ipintel",
        "adobe",
        "nvidia",
        "wix",
        "life360",
        "zapier",
        "x_email",
        "snapchat_email",
        "amazon",
        "spotify_email",
        "google",
        "scratch",
        "dailymotion",
        "substack",
        "duolingo",
        "duolingo_email",
        "dockerhub",
        "wikipedia",
        "internetarchive",
        "telegram",
        "youtube",
        "spotify",
        "patreon",
        "wordpress",
        "okru",
        "flickr",
        "whatsapp",
        "opplysningen",
        "ratsit",
        "reverseaustralia",
    ],
    UnrecognizedStr,
]
r"""A NoResponse source: github (GitHub accounts), phone (the phone lookup), breach (breach exposure), rdap (the email domain's registration), mx (the email domain's mail servers), ipintel (IP intelligence) or an email account source that searches one platform for an account by email address (adobe, nvidia, wix, life360, zapier, x_email, snapchat_email, amazon, spotify_email, google, duolingo_email). x_email, snapchat_email, amazon and spotify_email only say whether the email has an account on X, Snapchat, Amazon or Spotify. google runs only for Gmail addresses. scratch, dailymotion, substack, duolingo, dockerhub, wikipedia, internetarchive, telegram, spotify, patreon, wordpress, okru and flickr each search that platform for an account by username; telegram also searches by phone number, through a logged-in Telegram lookup account. whatsapp searches WhatsApp for an account by phone number. opplysningen (1881, Norway), ratsit (Sweden) and reverseaustralia (Australia) each look up a phone number of their own country on that site. youtube searches YouTube for a channel by username."""
