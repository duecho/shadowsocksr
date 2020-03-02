
def banbt(hostname):
        hostname=hostname.lower()
        if "torrent" in hostname or "bittorrent" in hostname or "peer_id" in hostname or ".torrent" in hostname or "announce" in hostname or "magnet:" in hostname or "xunlei" in hostname or "sandai" in hostname or "xlliveud" in hostname or "thunder" in hostname or "/default.ida?" in hostname or ".exe?/c+dir" in hostname or ".exe?/c_tftp" in hostname or "get_peers" in hostname:
            return False
        else:
            return True