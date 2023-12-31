from typing import List
from collections import deque
from collections import defaultdict

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        try:
            if n != len(leftChild) or n != len(rightChild):
                raise ValueError("The size of tree is not egual with leftChild size or/and rightChild size")
            if n < 1 or n > 10**4:
                raise ValueError("n value is too hight")
            childNode = defaultdict(list)
            visitedNode = set()
            roots = [node for node in range(0, n)]
            #Fill childNode
            for i in range(0, n):
                left = leftChild[i]
                right = rightChild[i]
                if left < -1 or left > n-1 or right < -1 or right > n-1: raise ValueError("Leftchild or/and rightchild have a unknown node")
                if left != -1:
                    roots.remove(left)
                    childNode[i].append(left)
                if right != -1:
                    roots.remove(right)
                    childNode[i].append(right)
            if len(roots) != 1:
                return False
            queue = deque()
            queue.append(roots[0])
            while queue:
                node = queue.pop()
                if node in visitedNode:
                    return False
                visitedNode.add(node)
                queue.extend(childNode[node])
            if len(visitedNode) != n: return False
            return True
        except ValueError as e:
            print(e)
            return False
        
assert Solution().validateBinaryTreeNodes(4, [1,-1,3,-1], [2,-1,-1,-1])
assert not Solution().validateBinaryTreeNodes(4, [1,-1,3,-1], [2,3,-1,-1])
assert not Solution().validateBinaryTreeNodes(2, [1,0], [-1,-1])
assert not Solution().validateBinaryTreeNodes(6, [1,-1,-1,4,-1,-1], [2,-1,-1,5,-1,-1])
assert not Solution().validateBinaryTreeNodes(4, [1,2,0,-1], [-1,-1,-1,-1])
assert Solution().validateBinaryTreeNodes(5, [1,3,-1,-1,-1], [-1,2,4,-1,-1])
assert Solution().validateBinaryTreeNodes(4, [3,-1,1,-1], [-1,-1,0,-1])
assert Solution().validateBinaryTreeNodes(1000, [38,27,5,13,7,6,34,9,15,33,50,30,51,23,36,19,18,22,215,150,26,93,25,42,152,29,28,204,921,109,32,67,44,56,280,151,81,59,97,78,513,45,43,-1,111,48,-1,149,72,107,178,64,62,54,141,386,77,161,136,289,66,75,101,944,102,112,224,188,120,71,260,80,154,248,237,236,160,830,83,172,86,-1,117,87,92,780,293,-1,95,212,209,104,731,187,207,118,-1,113,164,387,123,444,140,251,257,-1,647,407,-1,282,942,766,-1,227,146,130,985,119,-1,191,-1,250,131,373,142,709,427,262,-1,284,425,292,617,171,507,218,175,214,147,157,256,238,148,195,179,521,259,-1,226,695,190,-1,355,-1,708,163,308,173,180,-1,253,170,182,229,200,239,-1,186,473,322,-1,391,-1,411,244,486,-1,235,480,198,222,541,205,-1,317,196,814,365,555,281,389,-1,376,-1,593,-1,-1,339,231,201,202,210,208,469,354,252,223,341,-1,464,659,269,-1,217,672,-1,219,484,-1,241,395,266,962,379,-1,-1,299,261,532,475,307,285,254,413,590,268,-1,628,699,-1,249,-1,712,384,544,476,313,-1,401,-1,337,345,303,270,703,267,771,518,382,704,410,283,506,566,333,-1,271,-1,-1,319,279,-1,301,655,-1,-1,744,547,519,316,383,422,604,288,549,-1,892,905,-1,311,400,722,294,332,-1,420,364,454,855,-1,393,-1,650,690,943,654,542,329,957,326,988,-1,945,321,-1,357,490,323,-1,320,-1,344,675,681,737,330,689,515,757,966,951,361,774,916,350,739,-1,351,370,-1,576,891,419,597,416,605,574,390,-1,461,529,-1,694,-1,-1,616,677,434,-1,366,-1,-1,-1,459,-1,620,452,372,829,429,-1,-1,-1,470,398,589,-1,511,-1,385,404,-1,-1,424,495,846,-1,643,-1,625,415,403,876,-1,539,912,646,-1,-1,-1,794,611,-1,968,489,437,836,863,448,971,523,777,977,-1,720,-1,-1,706,-1,-1,-1,730,481,445,510,-1,-1,-1,-1,558,649,716,-1,451,-1,505,634,478,-1,503,-1,-1,-1,562,-1,751,-1,948,781,-1,-1,462,747,-1,-1,-1,463,504,-1,-1,474,615,745,559,901,614,468,-1,494,-1,564,800,-1,-1,563,-1,-1,839,-1,-1,845,767,-1,-1,-1,-1,581,-1,528,-1,639,660,573,-1,963,526,653,-1,-1,-1,-1,805,-1,-1,779,-1,667,548,914,-1,973,701,-1,-1,-1,609,-1,760,522,-1,-1,910,-1,718,-1,-1,584,913,-1,-1,960,-1,-1,-1,-1,-1,626,546,954,-1,-1,560,-1,-1,-1,685,-1,807,572,627,552,-1,-1,-1,-1,-1,920,-1,-1,879,989,927,871,565,925,811,596,-1,608,-1,-1,-1,-1,-1,-1,-1,-1,594,-1,-1,-1,-1,-1,-1,606,-1,841,651,-1,758,-1,898,-1,822,-1,664,-1,705,607,778,-1,865,-1,-1,-1,-1,-1,-1,809,-1,-1,-1,707,-1,-1,692,-1,725,941,-1,906,-1,882,629,-1,993,-1,-1,997,838,-1,-1,636,640,-1,-1,-1,-1,641,-1,-1,717,-1,-1,-1,678,874,-1,-1,819,-1,844,-1,-1,711,928,-1,-1,674,-1,-1,-1,-1,840,752,-1,936,740,978,-1,-1,-1,-1,-1,-1,-1,790,-1,-1,783,-1,702,772,-1,741,-1,-1,-1,-1,-1,-1,-1,-1,895,-1,-1,-1,-1,-1,-1,-1,915,-1,-1,710,763,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,820,-1,938,-1,815,-1,-1,734,-1,-1,-1,812,-1,-1,958,-1,-1,-1,-1,935,861,-1,-1,-1,-1,-1,911,-1,-1,-1,-1,-1,-1,-1,773,-1,-1,-1,981,789,-1,-1,-1,-1,-1,903,-1,-1,-1,-1,-1,-1,-1,-1,847,834,-1,-1,959,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,826,918,-1,-1,-1,-1,-1,804,-1,934,-1,817,-1,-1,816,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,872,-1,-1,-1,-1,-1,-1,866,-1,-1,-1,-1,-1,-1,-1,947,-1,979,-1,854,-1,926,-1,-1,-1,-1,-1,-1,-1,889,-1,-1,-1,-1,-1,-1,996,-1,-1,-1,-1,-1,-1,878,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,992,909,-1,-1,896,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,980,-1,-1,-1,933,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,955,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,964,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,986,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1], [1,2,3,4,8,10,11,47,89,12,14,21,20,70,304,16,17,68,24,197,35,31,40,39,37,90,53,65,46,-1,58,158,99,124,168,923,516,69,79,41,76,61,74,52,49,165,169,-1,88,432,199,63,496,57,55,60,128,73,137,145,121,115,135,203,443,85,110,318,127,91,100,133,84,623,153,225,98,275,138,82,183,-1,116,125,213,181,296,94,96,-1,106,103,129,309,-1,166,220,143,108,-1,144,263,185,114,105,194,848,893,-1,409,193,159,126,192,-1,174,613,122,132,134,810,394,586,206,156,228,569,155,162,485,139,-1,430,167,-1,176,-1,362,258,221,450,440,230,-1,446,408,669,-1,857,-1,982,331,352,240,561,-1,177,754,242,-1,312,-1,-1,246,211,456,189,298,233,502,232,358,472,184,-1,367,-1,-1,234,-1,273,-1,247,467,243,388,340,245,287,381,305,-1,264,759,-1,335,347,-1,342,-1,300,216,-1,255,907,265,743,-1,492,423,356,371,314,-1,-1,578,-1,493,338,272,278,756,442,545,325,471,600,277,635,327,295,642,276,377,579,297,353,-1,397,-1,349,602,-1,-1,-1,336,-1,806,465,-1,286,418,334,-1,483,369,-1,746,466,-1,-1,449,582,328,274,436,324,887,796,378,479,302,306,291,514,310,290,990,688,406,-1,637,346,-1,-1,363,-1,924,956,-1,-1,568,832,644,886,624,497,-1,-1,-1,-1,417,525,375,343,315,670,-1,-1,585,554,359,380,399,683,531,786,396,374,-1,869,421,733,-1,-1,-1,348,553,867,842,-1,-1,431,392,512,368,435,601,726,719,524,538,-1,587,477,808,500,-1,-1,-1,618,-1,-1,441,595,661,987,-1,414,360,598,-1,622,439,662,-1,498,742,588,922,-1,402,-1,-1,-1,460,-1,-1,405,551,-1,433,535,530,687,-1,556,482,-1,-1,-1,537,-1,-1,-1,-1,-1,426,-1,828,412,939,-1,-1,455,970,770,732,499,-1,527,-1,-1,-1,501,428,-1,570,630,849,-1,-1,-1,457,-1,686,-1,438,631,509,930,-1,714,447,769,533,-1,-1,536,801,-1,673,-1,775,663,762,-1,-1,453,-1,-1,-1,-1,-1,543,633,458,488,696,658,-1,657,-1,994,540,803,-1,-1,835,-1,517,870,487,-1,-1,831,591,851,577,-1,931,-1,508,-1,-1,818,550,998,491,-1,680,795,-1,610,-1,592,-1,-1,937,-1,557,632,-1,-1,-1,-1,761,520,571,-1,-1,-1,-1,995,-1,788,534,645,668,-1,-1,859,-1,575,-1,-1,619,-1,-1,-1,860,-1,-1,-1,665,-1,864,-1,850,612,-1,-1,-1,-1,693,949,599,583,-1,671,765,-1,-1,-1,-1,-1,793,691,-1,567,764,603,946,580,753,-1,648,-1,-1,638,833,884,-1,621,-1,-1,-1,-1,782,697,-1,713,679,656,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,932,749,-1,902,-1,-1,797,-1,-1,676,883,727,-1,-1,813,-1,-1,-1,-1,-1,858,-1,880,984,-1,-1,-1,-1,823,-1,875,-1,-1,-1,-1,-1,684,-1,-1,-1,-1,-1,890,682,837,698,776,-1,784,-1,-1,-1,-1,-1,-1,652,-1,-1,792,715,-1,724,827,940,-1,-1,785,-1,750,900,-1,666,-1,-1,969,-1,735,-1,-1,-1,-1,-1,-1,-1,721,-1,-1,-1,-1,729,972,-1,-1,-1,748,-1,825,738,-1,999,728,-1,-1,-1,700,-1,952,-1,-1,-1,-1,-1,-1,-1,723,-1,888,-1,736,-1,-1,824,768,-1,-1,-1,799,-1,917,-1,843,-1,885,798,791,802,-1,950,-1,-1,-1,-1,-1,-1,-1,755,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,983,868,-1,-1,787,-1,856,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,899,-1,-1,-1,-1,-1,-1,-1,-1,-1,877,853,852,-1,-1,-1,-1,908,-1,-1,-1,-1,-1,862,-1,919,-1,897,-1,873,991,821,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,904,-1,-1,-1,-1,-1,-1,-1,967,-1,-1,-1,-1,-1,-1,-1,-1,976,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,961,-1,894,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,953,-1,-1,881,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,929,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,965,975,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,974,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1])
assert not Solution().validateBinaryTreeNodes(6, [1,2,0,4,-1,-1], [-1,-1,-1,5,-1,-1])