function shortestSubstring(s) {
    // Write your code here
    let arrS = []
    let splitS = s.split('')
    splitS.forEach(el => 
    {
        if(!arrS.includes(el)) arrS.push(el)
    })

    const checkSubString = (substr) =>
    {
        let temp = substr.split('')
        for(let i=0; i<arrS.length; i++)
        {
            if(!temp.includes(arrS[i])) return false
        }
        return true
    }

    let smallest = s.length
    let j = arrS.length
    let smallestFound = false

    while(j < s.length && !smallestFound)
    {
        for(let i=0; i<s.length; i++)
        {
            if(checkSubString(s.substr(i, j)))
            {
                smallest = s.substr(i,j).length
                smallestFound = true
                break
            }
        }
        j++
    }
    return smallest
}


console.log(shortestSubstring('lybgvumnwehjxoswnprlhvsuzvgyeettenngipfvrflpprjjalchhhcmhxkupciulccqssaqgdttpldmzdzveslyjadswtsbhgkddeouxbldsxzmfvhtonlampljgzyvemxhnlcrldtfthulkxhflcoupgeikrlaksuyfqvnvtnqspyjbxrnphouoyhvlswvoibuvbhhjcdflvlxrgorfbjrofokggafxmdqhqatsfezchpicyuawpovmmyzwforhkoatppybfofhdzsbiyjldsklgznfnqydisnyxzfpoftcjuprwygsnxkikqlimalfgxnuohrnhgqpublurhztntgmimcozuufzphdyiucrmmmjqtceykwnnbqorghzyzzukjqsjbmpfmdtrgvwvyeikgjdnmlxkxwldnmizapzuhsbssaxjutkbkoljyodlipofvnkqkktwtjlvgmkgjwlectlagylwdvomtuypjbtvitkqnnvtdxwrclpspcngrdrlsvyxfeohtupjvmyctacnifdnoryahqghzhoqprgkymyphiuvdvgjppfdgpouzjwbqkhqoyefmugjvewhxusqfzwuweifnsbijkeepyxrysojacqthkcijbzpmqfbmnrhybaibmzonzqlnmdjsvofgjftyfehikljfrfgznuaytvaegmaaljhrxtodjqxogwaxrssjxgvnkawzaqswwofedxjflugpktauixpzdckodknlbvxrsrjeobuvvqythyvzxbcgrlbgchwcperpbaxqbujxcxcklrrklkbnwlrwyuygzmgbyyhgapxwdbycdunhtedgvsrhchoxqwrssuhesetvejonqwhkwezjvjggmsqqyrxtjkcalswqqhvyimheopjzdkmouegzbphmgoxqwlbdlcumdgixjbcqvztzdjqmadthtdmvaqcagsyqggcfiifcoktjpjxcjyiwchyicqibxdgkqtgqiwpdklhumzwljmgdmicmunnnpdbamofynykqvsijsnfkpfyptlmqpoyjmeqvhcrvgmqmqopusqktdthpvztfzxrnqbsqtipqonxtsnasonzvxbpipyhhbtopsuqomfjrdyislifqgbndakaqbbwnkxnwpzeoohlxuhrtbfnqorfguvomeepxoffghmatidzfpfnwbfujdonlvyvwcwcchvsasdylbrrxfcztzqopdihybrhodjnmoqkijywkoncvrjozdphbfaalexgtpdtkzvsebevsopjvciwljfkrcumyacqdapwczenvmabkapuoudipbozezeygljfftvycbvazmzbndlfvlsqiaixdtbhqvlzdmffjfbfsvthrfmkoxbhokcvethucgqyvopafyttrhesvlbgihetenaiqyufxffdwqvruhvuzxukffmudygjavemzdccamymhppwofwgjkykmqfbuujzxhlnckmmcuflzandlltowjpwsaljtfapfvrmezbsjxsswiwjscisoqlhahzaplclkwlrgcdqbcdwbwafgadgtcpgowefkaqjuffuguqepwnfhbnbuinlicpdxfesoxcfqclfnrhgsxkhxgxrcorfygjxpiqmwtqjwbhghmlocnfkglorkkvxznlzdhucvayrzfazefobxutitrfkrlrstkcbtikklmhmggklsbphcejuylhxnraoenhdpzngyodiqlchxyycxzrrbhfwohfvxkrzolrglgnvcpjesdzygyoifoygphqqevqjugiuahmvrxgaujnyclcjqxevhyfnlohavrjlbyyvhghxhywekedhvwytysljsqminajfipdsprglnpxfqwuvcibpynkxgxsupmbntqrlwyampdgunigxldhlhqdyjcfhuqjfymrbafmyocttyjmnhlfnrtzddlazixtlxyvmvfbiguhsfuqoerhymsnoprkbdlchswocbbwwdvastaiamnepwkyaqmpliruphedkxjqzgpexlwulswtvotlgotlncpvnrrzerzdygeraoozbttnyyifkindeouuagqgztvqdolfrzrlzddjzcshvdgkhxkdxflwxmejkkszylbhoaacicwqiizickgcdxstpzkskjwdqegrearjrncmmkdelekbesuhquepjrnrzbllldgdmyrpglrhllwnqozfudjpchowhwevbqvjjezsmhylnjpktbspxnktxkmcfxwiaqqbhqjwufmwresfsfaokeaaadziobioqmtsvjgzkgkhbzpaeuexyudhrioicyqsjmngrwqpoherwuvdgeruffmlgphwbxzovyewtfazfpmvfvyguqditjlxnoixsyghyfrdngjfblyveibcapetpmeaidrtpnwwiifhpfgsptkvhhwkzvtvlhhbipjxurgqbtldimsarncplkeweoirjenakyprzzphewoprwyvfpjyglzrmhfqpdubheeqtgrmbxlcmnbtaqakgimuapsbuxzokhwnykughmwrlkjsvtdlzwpbhcsbvjnomutffmjggrmyilgschgwrrztnmvndmuahvnlwpwtglvbtkegzjstpiwllpgnlpcnezqscxkelindfvurtxsezrwzvzechocnvfaimxrqnyiqlybugjsblhzfravznkbtgcpqwovwpxzgxgodlhmixisfzdknoxzasscewgzvqkxuqrsqxsfwdwneyqisozqjfgrvhfsfeuspujvqhydwveadosqafyxbmzgrotyffqblolplosqnfcwxiuwkldpuenodlvotbqiizudxqjvfnkyicjcywjkfvukvveqhjrxdcigwbjdftdyelydzyummmtzuvfmaicednymxoaiuhigfkfavgeemcgofnaefganqoniqebfibigljbceulicojzjfrceigxprunjncymbrljfqmwciqtyncafzjyagimmzuejrttefhdwqcizyiurxvfbwrjxffzbjexshvwrxwrmhrbdxjwipsdfhtknfaswfrvxqdkhbwwefbvqsghhhutdgethcwupzrtsbhbjnbqwpccoaonxwvkhowbzhaoscgykzbiltlwqqatyeczzceuuwgvjxzonhkkfjcbwsezdmifdegsyjtswselknxweimxlnzohgtqthlftjblnphtdwwvsscbhjmruuqscwjpynxbkoomwdecqkrtbxgzgcxhppcjnqtcfqttkkolzcfikwblxkimijeglxsvcrkcqjjwcwuhvzydmegubqavlqffhrzzrhiwxrgftittdxcaybczncsyjlzlxyyklcppoxcgnexmaajzuhabdhaccuualacylsmtkewbprsmoncggqvrvsqqoffmwkplsgbrpurgioajuppvqluhbdetzdzwwzaelmopafumtqugecywglucmugwqiizveswrjevfzdnxlbkakrpzcejvxzeoybbtfdsvewjsivwswzjhudtpqsfclzcmukotirrxxtzksmxnjumofzhhowyftzfzbotrokaxaryxlkmueolqkrdxmzhoqnzvudeowcjloesfmqgvxwfyhnpbepbvbgjtbvqpoeugoqynkbfivmfewjjscjreixyqssxzsydgllfzmobnurxkwcypctjkabigwqtldwhjouaswtovdtkrlonzgeyddkqwuhnimzffxviyvsktqrfafqujhdepvczzhiyjlkxmeplnrvxgshdykehkefpkvepcxhozpjxtreynyliguhuxudbnhmfojordxzmmklgohcmmbukzshyrmooliaobbnlapadutnbetocxylceyxywdsjegdfcrsblbxhjsgcuoxmqftytngzdcmsrfyjjumcbxoleldazwzwtdjoyuqeqjfxazjarqgfmsfxyfqbeoktcctnfqrsjchxpqiltaqzawhguusgenjcfxriyfikpgdvwhbyumthkiktbecjwalsxqjyajrkcvysicisabtbrdeumbvtviihjwxdczpdnrrgmemxydgxlrjzucxyidwcdvdpvjlagwmgcngnpxjkximsogvyhnchlimsxcjwtrijtizpezjlcqekojrrjzvtvhnqvieqmdiedzqswrsnfmnneltcutqfcqyrrwmnwtelvsqrruwfjwrhjcrtbcytnyqmqxceuohpiffaqnrmoybqjjgdyotpmxttqftypfexlvdtgxqafiqbqjlnpbflkgaynkddbzllecdctccvslpdcurkxfoimnwdfvnyqkzlheruxrmiiygnzfovnrwcoqsgoameiunvzemmxtklistlxuynrwsjaxzwmhktdayzzoxbbemejgosgcynfapykbc'))
// while(i < s.length - arrS.length && j<s.length)
// {
//     console.log('sbs', s.substr(i,j))
//     console.log('i', i)
//     if(!checkSubString(s.substr(i,j)))
//     {
//         j++
//     }
//     else
//     {
//         if(checkSubString(s.substr(i, j)) && s.substr(i,j).length < smallest)
//         {
//             smallest = s.substr(i,j).length
//         }
//         i++
//         j = i+arrS.length - 1
//     }
// }
// {
//     for(let j=i+arrS.length-1; j<s.length; j++)
//     {
//         if(checkSubString(s.substr(i, j)) && s.substr(i,j).length < smallest)
//         {
//             console.log(s.substr(i, j))
//             smallest = s.substr(i, j).length
//         }
//     }
// }


