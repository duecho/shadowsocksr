import re
def banbt(data):
        m = re.search(
            '(announce|/default.ida\?|magnet:|peer_id|bittorrent|torrent|.torrent|peer_id=|info_hash|get_peers|find_node|BitTorrent|announce_peer|announce.php?passkey=)',
             data, re.I | re.M)

        if m==None:
            m = re.search('(.*.||)(dafahao|minghui|dongtaiwang|epochtimes|ntdtv|falundafa|wujieliulan).(org|com|net)',data,re.I|re.M)
        if m==None:
            m=re.search('(.?)(xunlei|sandai|Thunder|XLLiveUD)(.)',data,re.I|re.M)
        if m==None:
            m=re.search('(^.*\@)(guerrillamail|guerrillamailblock|sharklasers|grr|pokemail|spam4|bccto|chacuo|027168)\.(info|biz|com|de|net|org|me|la)',data,re.I|re.M)
        if m!=None:
            m=True
        return m
