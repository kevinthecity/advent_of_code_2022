from collections import deque

def is_collection_unique(my_list):
	return len(my_list) == len(set(my_list))

def parse_elf_code(code, packet_length):
	chars = list(code)

	window = deque()
	i = 0
	for char in chars:
		if len(window) < packet_length:
			# get to packet_length
			window.append(char)
		else:
			if is_collection_unique(window):
				return i
			else:
				window.popleft()				
				window.append(char)	
		i = i+1
	return -1

codes = [
	'mjqjpqmgbljsphdztnvjfqwrcgsmlb',
	'bvwbjplbgvbhsrlpgdmjqwftvncz',
	'nppdvjthqldpwncqszvftbrmjlhg',
	'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg',
	'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw',
	'dfsfmfbbbjnbbpddfcfjcjbjwjqqbtbntnhtnncfnfpnffwpphwppvbvtvztzszfzhhnqnvnpppmzmczcmzczbznnbssbhhvghhzqzvzttjvtvcccdhccmvccgdgttghthppwlwqlwwcswspsfsdfddhwwzlwzwttlglttsjjthhgcgfcfhfhtftrffwcfcsfccnntmmpvpgpfgfsgfflgfgmffbmmqsmqmmcqqmjjzczwczzpjzzgtgnnqqvdqvqllbttftgtztcztttlslrslrlfldljlwjjnvjjmrrhdrhhflhffgnfnjffmvmvjjspsvvrcchhgngwwdwbwwfhwffmggbsgspsjsfjjdwwbtbdtbdbgdbbbzhzvhhwpwlwfwfswwrgggmggssfwwdrwrccssjttltrrnggdbggvzzzrfzfwzfffnfnmnnzmnznpzzdtzdttbvvgffmnfmfmbbqppcgpgtgpgggcwwlpplslbslblhlmlfmlmldmmjhjjgllglhlssswcssprrqrjrhrvrffpfnpfnppzgztgtdgtdggftgftggqrgrnnqpnpgnpnggsjsvscsnswshwswfwfwqffcrrmprrrcgrrggmnnmzmwzmwzzgzzhnzzthtggtmmdrmrbmmqwwjswwphhzvvjqjrrvzrrmssdvdlvvlhvvjggbwbrwwjqjqmmfllttvpttdvtdtddrttpltpllzrlrwlrrvcvpcphcccqwwtpwwbmmtntfntftvfvfqvvwnvwwvhhlccvrcrlclcqcvqqsvvfjjqmmfhfvvctczzlhlsslpspfsswnsnzsspzpccmssmpmbpbmmvnvsnvsszttrppvgpgnncllrvlrvllcvlvwvhvghgvvnhvvmffclfccvwcvccrwrhhrffqrqcrqqhbqhqssmzsmzsmmzrztzllmclmmbgmbbrmrgrwrgwrrgngvvtqqpbqpppgbgccsjjcmmtdmdjmmjcchvchhbccnjngjjnwjnnrvnrrsqshshszzqnngbnnrnggvwwlzwwlqwqmqdqrdqqrhqhffpgffqgqdggfjgglfglgvgjvjmjtthghrhvhgvhvnncnwcnwntwntnjjqjwwrdwddsggfddnhnsnvsstbbjddfhddhbddwbwbnbrnnrhrqhqdhdllvbbnzzbmbttpjjngnqqcffrsrnsnnhzzgllgvlvcchfhzzmzrmrggdvgvgqqwnqqpdqqvjjvnvhnhhgvhhgllhlzlclbcccwppztzhhvmvzzzsbzbppvdvdtdtdvdsdlsscnnqhnhgngghrrzprzzpddmvvhcvvprplpnlppscctzthtptspttmftmftfjjdfdjfjrfrfbfcchmhnnbddwzwvvpvrvnnslnlnhlnhlltslttqpqvvgzvzsstcstsrtrbtbbzmmzrzqrzqqnmqnnpjpttwgtgzgqqgmgnnzgzrggpbggvssqvssmhmshmssvlvlmvvnhnhddwbbllffgbffbbztthbhdhdghhrccfmfrfmmbdbfdbffzfgfrfqqptpgpjjlvvbjjdzdbbszslzlldnngwgddbmbpbwwhphnhmhhlthhgfhfvvpmvmhvmvdvsddsjtzvfmpsrwrrzgcvnnllfjmvfptwncppfmgqbfzrdpnfddghsqfmnqfwfslrsgjmqtfqwhdddsbhtbtpswcbfppcbhzfzbsqljzndcsrlhrrtstgfhhfsqqrwgnncsmstdmjvfjhqnrczlftzzzhqdzjdcdqcgfpmbqntdhzcvbtpssrvmgjwzwfvtpsrsrwrvrsjgrmzqzvbttscldsnnwzvmlztnnpdjrwvhshpdwgvhmlrnhtfccjnldlnhtfncfjjjztjmhrdqpvhggtqzwjsvwdzhdmwhsmgzjcwzqzlwbrlzsmlwhpjvflnppvrbgrsblmjpnqvgpjbpwbjgjqzwvjbgcplccjgbfwlblzfjqpwszbqbcnlbmfmqpmgspscgfdgfwnmcdzcqnjznndjcvlblszcnpflbjqltpfzhffdbwbshtpnwwlspltpcrvbdtflwbjrfnvrflqpgqtjzqwmmsdvtsmgjtrtbrzchwhpfsznjqcbrjcvwqgrcsqpvfzhrdlmnvvhjzpgpnlrmqfvcnlrlcfjblfcgvngdjfdczsrtnnwjndsfcsdlhdnbtplfnhsmmbldmsjwcblghhgqwbnjvqbqhddrmrtncvwnchsfpddzgrrtzntmwnmdwlrvnjgnzjqvptztnqnqmcjmmrhmtstgdvhffbbmphnbtsdmpmscsfdbnfnchrhhjpsfhhswfszgqfcbdbgnrqhrflpfgfgdcrjvrwbvsfmzzhvzvqzgshcqzlfcljnlgshdlhwdchhhvwlshwdrgjfbnptqqglbpcfgrmqjhqvlbzdwgnzfzlpcpjzqwhbfjljszvjdsrmfzntgnjflhnwhpfrlbpvgzmbqwzlgphmbvbfdqfgqqbhzzvrjftnwjzhlrqccwcfzvntscnbfcsrqqnvlvhszpgwtrzjrqbtslctbhtbczwtmsgwczncbjmzqvnthpwjmsbsjnfpsmghnvtqjjnjfwtnmlthrlcpqhjpnvnbbnwrdjfshwhpdwmsbngfhbhsqphlqspcgzwrgfjmqqtlsfgnvqtdgnhmdvvqzjwlhsnvjczbssrnlhwdmdthmtprjjfttfzbbswfwsvvslfnbcvprzhtcqwdrzjrnjjctqfsjrsddlhzcnstqfppjlqhvcbjbfwndwdtdfvnlwgvdvhzzrqthdhdmddfdwschmpwwrnlgsldzhgjrlmtzrnrrtqfctvbncpcjlsvnwjvhgnbshhwlqhtjghvrctlvngjgjrlgshhwscrdvzjqtfrrbssvqlcjjdljpmlzfqqnqmffpsbvgcqzqdjwczbqwjgfvpdgjglnqdshppcsqcmszhrbcpnhjnczlhwsbnfnzsczjvmftngqcvhgpgwlzbmjnmmdvdjfrcwnjrncvfstrvvqsstphmqdpwjqhzgppmgwlgjhgfwqgmjrlsvqpfqznvbqzgtngvpbpttzvngjwtrjgdnvdggzlnmpgbzhtnfnrhgwvhnpqdwfdvvftzllpqblgdglclwtwbchlvwcmmvtchlntlghztfvgfjczcbqmzgnqmrjcmqvjmjhfpztjcvclblmrctzfmsdfvfpwdcbsglgrsjqcgtcblhbtgcgjlwhhqnwhdnwzlhvphtvmlfnbfmgpnnbzqtdtzqrbhfljlwstlbscnrsvhrbrcthvzcngrttddcjqhtmsfpsgldgtsgjtprsttlssmrrfjmrddqvnqcfmphbnjtdsqvptrdzqbqfjqtnrqtjgdpbrlzrlvwcbcqbcmncfmwcpdhgpjdrdcmrqnflsqbllrqslmhsljwghnwcjwvhchcnlgppmphbqtcdfzjpcqcgsjzvmgfjgfsvmvjfqvtpffbpmhnnnrjmqhhhrhrqfqdwzdvzssslzvqhngdpszztgrvjntcpzhbfmhbpvcndsjbtnwgpmztpbrtjmfqrsvndrspdqmlsbldgghfflncszhnsttfslvwhvfnsmmhbbvjqslsjfqplndndwmbmvgchgvhzclrcnhvgbgmpctrggvqpvqvgvncmdwhpmwhzwhlgsnlnwggfbbvdvqrrsmhwzrrpgrjfshzgzjpfwjhpqmqhbjlwhwsfszlshpzprvgprlprrvlcrmbttjrpqsrdcdfwdrzbcfjpvrlrjjdwhbspqmrblvtldqdhtjtjphpqswgvqfftdgqrtjgsmthlhvlcqrwlqtthwjgrcpwcnsqtssqzpzqptrwjjdfchfmmsrsccnlvqbdmbcdjmhpgvnnlttfhggfphvbwqtcztbnsflztcfpbcpjbcmsplhjdbsmzhgnmfrhscmwmfqbljvhgllvvgqzphzbswdzlhmpcvnntczrcnqvlphhjdjjjnhfzzcjjsdlfccwvswvjfgvmlnpvjvcbpglsgtpj'
]    

# Part 1
print('Part 1')
for code in codes:
	print(parse_elf_code(code, 4))

print('Part 2')
# Part 2
for code in codes:
	print(parse_elf_code(code, 14))