# International newsroom

The homepage contains 10 editorial slots of about90 seconds: seven verified live broadcasts and three selected official news recordings. Initial allocation: US30%, Korea20%, Europe20%, China10%, Japan10%, Qatar10%. This is an editorial weighting, not a measured influence ranking. Actual viewing share changes when channels end, block a region, require sign-in or fail.

Player: official YouTube IFrame API; muted autoplay; explicit retry; 90-second visible exposure countdown; pause offscreen or in hidden tab; resume on return; skip errors and nonadvancing clocks; bounded cooldown; stop with original links if everything fails. Pinning stops rotation but does not override provider restrictions. No stream copying or paywall bypass.

CNN HLN is not the same as the selected CNN recorded news. HLN official access guidance requires a participating TV-provider subscription. Do not relabel CNN clips as HLN.

Refresh uses the existing regional slots. scripts/refresh_favorite_news.py proposes source changes for review; it never converts a blocked discovery result into a new verification timestamp. Review current live status, official ownership, embed permission and actual playback before publishing an updated manifest. If unavailable, preserve last verified timestamps, identify the failure and use browser/source checks rather than silently declaring the list fresh.

The old bottom portal remains stored unchanged inside preserved-portal but is display:none. Its visible navigation is hidden and the main browse button opens the current searchable article archive. All144articles,135leads,4142reference entries and existing per-article broadcast links remain. Existing consultation UI is detached from the hidden old layout but its recipient route has not been changed pending a verified direct chat URL.
