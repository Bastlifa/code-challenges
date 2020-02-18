def acmTeam(topic):
    topic_b = [int(t,2) for t in topic]
    def count_zeroes(bin_str):
        count = 0
        for b in bin_str:
            if b == '0': count += 1
        return count

    zeroes_dict = {m:None for m in range(len(topic[0]) + 1)}

    for i in range(len(topic_b) - 1):
        for j in range(1, len(topic_b)):
            comb_str = format(topic_b[i] | topic_b[j], 'b')
            zeroes_dict[count_zeroes(comb_str)] = 1