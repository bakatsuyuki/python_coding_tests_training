from typing import List

from line_profiler_pycharm import profile


class Solution:
    def __init__(self):
        self.chain_map = {}

    @profile
    def longestStrChain(self, words: List[str]) -> int:
        result = 1
        words.sort(key=len)
        for word in words:
            if len(word) > 1:
                chain_value = self.get_chain_value(word)
                self.chain_map[word] = chain_value
                result = max(result, chain_value)
            else:
                self.chain_map[word] = 1
        return result

    @profile
    def get_chain_value(self, word):
        chain_value = 1
        for i in range(len(word)):
            before_word = word[:i] + word[i + 1:]
            if before_word in self.chain_map:
                chain_value = max(self.chain_map[before_word] + 1, chain_value)
        return chain_value


for _ in range(100):
    print(Solution().longestStrChain(
        ["jmhzmzqqhyqsgxux", "cfawfi", "nf", "gmdnwlrfatlid", "dcjkwhp", "rimtnlwlv", "qidgztolactna", "jkemexmp",
         "thhvstcrmyx", "uvkgdbja", "ceutfdpdeu", "ccqedvarwcv", "ugmdnwlrsfatlid", "ritnllv", "dasbrcxcnpg",
         "lcucqoeudvparwcv", "hzqysgxux", "rarefcgze", "tnmj", "mxigwxdnwqdrxt", "gr", "qfjihkfx", "kkqheaecnzlywm",
         "arcxnpg", "qseu", "xmcifhpgbeblx", "lcucqoedvarwcv", "jmhzzqqhyqsgxux", "fzlnty", "wdjlbvf",
         "qidgztolacqetna",
         "mhscxwryzihcxy", "giqotytadnwy", "xkphnrftfsy", "dcaieoxcltro", "jkeexmp", "xkphnrfsy", "fjihkfx",
         "hswyzihxy",
         "wuzwuyx", "mjrkemexmp", "caioxcltro", "jkeemp", "gykybuv", "yuv", "y", "rarfgz", "gixqotytadnwy", "emrmo",
         "mxigwxdnwqdxt", "rarefcgpzte", "icfzcpzlnty", "bje", "cff", "yv", "qqdqgkwzwr", "j", "yzersgxslkktn",
         "oaudxkww",
         "soqowqlze", "jvopdyivokd", "hbqwe", "nsmgtonw", "bbjs", "ysoqowqleze", "hhry", "illv", "hhtry",
         "bqfjizhmlknfx",
         "zlhaizailfku", "mjrkemezxmp", "xkr", "rnbbbnibxk", "nqsrxdezjuo", "qsrxdejuo", "thhzvtstcrmyhx",
         "kkqhkeaecnzlywm", "oaudyduvxkvwwy", "cpnozxtvkfhldwqk", "gybuv", "rnarefcgpzte", "hswihxy", "bjpjmckyjzyylb",
         "wiuzwuyx", "ntf", "bqfjizhmlknfvx", "gykvybuv", "owndoqjlbvfy", "wtlomktdx", "nmqsrxdezjuo", "vffjtdloqdbs",
         "gykvyybeuv", "xmncaifhqpgbeblx", "aoxcltro", "oaudydvxkvwwy", "jwixjcdwe", "owdojlbvfy", "kenlywm",
         "zlhaizailfoku", "hhstcrmyx", "wtmkx", "qqkwzwr", "wlbv", "zbhwa", "rimtnlwglv", "dlzcjwkywhprr",
         "zmjrnkemezfxmp",
         "xkphnrffsy", "nsmgtnw", "kqeaecnzlywm", "jvopdyvokd", "jhokxe", "mmo", "wbzkxdkhivvsws", "qidgztolacqtna",
         "jmhzzqyqsgxux", "gdasbrcxncnpg", "bwbxhcujle", "qsrxdeu", "uvkgdbj", "mj", "enlywm", "oauddvxkvww",
         "wbzkdkhivs",
         "giqytadw", "thhvtstcrmyhx", "wtlsopmkqtdx", "xk", "qrimtnlnwgalv", "bxhcjle", "ysoqowqlze", "hhtcry", "itllv",
         "oaudydvxkvww", "uvkdbj", "mjkemexmp", "xkpnrfs", "jhfx", "wbxhcjle", "wtmk", "gryv", "jhzzqysgxux", "uww",
         "nmj",
         "nqsrxdejuo", "bxhjle", "bxje", "xkpnrs", "r", "wdjlbv", "cfawf", "mxigdnwq", "qidgztlta", "jmhzzqqyqsgxux",
         "qidgztolacta", "caieoxcltro", "caoxcltro", "owndojlbvfy", "elw", "ugmdnwlrsfatlikd", "xkpr", "kqenlywm",
         "kqeenlywm", "foycqrkuaqrbvm", "qqgkwzwr", "arcxcnpg", "lcucqoeudvarwcv", "jhokxem", "wbzdkhivs",
         "gvffjtdloqddbs",
         "yqvalr", "axcltr", "flnty", "hhtcrmyx", "gtaw", "itnllv", "giqotytadwy", "jke", "qqdgkwzwr", "qidgztlacta",
         "wtlmktdx", "ccqevarwcv", "hhtcrmy", "arz", "dcaieoxcltjbrdo", "bqfjihlknfx", "wiuzwuyyx", "oaudvxkvww",
         "xkprs",
         "bxjle", "rarfz", "qrimtnlynwgalv", "dcaieoxcltjbro", "xmcifhpgbbl", "kqheaecnzlywm", "b", "jvopyvokd",
         "ysoqmowuqlenwwze", "cpnozxtvkfldwqk", "yzersgxslvkktan", "udxww", "byqtfjizhmlknfvx", "vbqfj", "fjhkfx",
         "foycqkuaqrbvm", "dcjwkwhp", "zmjrkemezfxmp", "yzersgxslvkktn", "dlzcjwkwhprr", "vnismgtonw", "owndoqjlbvfyl",
         "xmncifhpgbeblx", "wtmktdx", "bjpjmckyjzyyl", "gykvybeuv", "gmdnwlrsfatlid", "wtlsopmkqtbdx", "asbrcxcnpg",
         "qqkwzr", "tmk", "zbw", "ifzclnty", "ysoqowqlenwze", "az", "rnbbbibxk", "flty", "giytadw", "axcltro", "xiw",
         "ceutdpdeu", "wtlsopmakqtbdx", "bjpjmckyjbzyylbf", "gmdnwlrftid", "oaudxkvww", "soqowqze", "ts", "jpjmckyjzyl",
         "qqkwr", "ceutpeu", "cf", "pemrmcoio", "jwixjdwe", "qrimtnlwgalv", "mhsxwryzihcxy", "kqeecnlywm", "cfwf",
         "xigwq",
         "zmjrkemezxmp", "hsxwryzihcxy", "xmncaifhpgbeblx", "arfz", "w", "gyuv", "hhvstcrmyx", "giqoytadwy",
         "wbxhcujle",
         "gytaw", "hry", "ceutfdprdeu", "gryvffjtdloqddbs", "zlhaizaidlfoku", "owntdoqjlsbvfyl", "cfaawfi",
         "rarefcgzte",
         "mxigwxdnwqx", "emmo", "emrmcoio", "wbzdhivs", "hswryzihcxy", "emrmoio", "yqvar", "icfzcgpzlnty", "uxww", "k",
         "zlaizailk", "jkep", "ysoqowuqlenwwze", "flt", "bjpjmckyjzyl", "qfjihlkfx", "xmcifhpgbebl", "owdjlbvfy",
         "wzwuyx",
         "cucqedvarwcv", "wdjlbvfy", "enlwm", "jhx", "mxigwxdnwqdx", "rnarefucgpzte", "icfzczlnty", "enlw",
         "foycqrkuaqrbvmy", "uvkgdfbja", "jhzqysgxux", "dcaieoxcltjro", "dasbrcxncnpg", "foycqrkuabqrbvmy",
         "wtlsomkqtdx",
         "ysoqowqlenze", "rarfcgze", "mxigdwq", "oudxww", "boa", "dlcjwkwhpr", "bj", "tos", "xiwq", "giqytadwy", "qqr",
         "foyqkuaqrbvm", "oaudxww", "gytadw", "icfzclnty", "bbjzs", "rimtnlwgalv", "dcjkwp", "wdlbv", "iw",
         "dlzcjwikywhprr", "zlhaizailk", "qsreu", "asrcxcnpg", "rimtnllv", "wzdhivs", "bjpjmckyjbzyylb", "bqfjihlkfx",
         "icfzccgpzlnkty", "ysoqowuqlenwze", "gry", "byqfjizhmlknfvx", "wtlomkqtdx", "foyqkuqrbvm", "wiuvzwuyyx",
         "dlzcjwmikywhprr", "vnismgtwonw", "wbzkdkhivvss", "icfzcgpzlnkty", "gmdnwlrftlid", "gryuv", "vffjtdloqddbs",
         "vnihsmgtwonw", "rarfcgz", "grvffjtdloqddbs", "wtmktx", "mxigdnwqx", "hswyihxy", "jkeep", "qsrxdeju",
         "nismgtonw",
         "f", "xigdwq", "vbfj", "jhkfx", "qidgztlcta", "thhvstcrmyhx", "zlhaizailfk", "pemrmcoiqo", "foyqkqrbvm",
         "foyqkqbvm", "dlcjwkwhp", "wbzkdkhivss", "webzkxdkhivvsws", "kqeaecnlywm", "emrmoi", "webzkxdkhivvswsu",
         "hswryzihxy", "bw", "jx", "ceutpdeu", "uw", "cucqoedvarwcv", "dlzcjwkwhpr", "ceutfdpbrdeu", "qdgztlt",
         "qidgztlt",
         "mo", "qsrxeu", "bqfjihmlknfx", "jhokxfem", "ke", "qqwr", "zbhw", "wbzkxdkhivvss", "zmjrnkemezfxmgp",
         "mxigwdnwqx",
         "owntdoqjlbvfyl", "fzclnty", "xkpnrfsy", "jhzzqyqsgxux", "gykbuv"]))
