from day02_data import data

def check_report(repstr, ignore_ix=-1):
    levels = [int(r) for r in repstr.split(' ')]
    if(ignore_ix > -1):
        del(levels[ignore_ix])
    
    # all ascending?
    b_ordered = (levels == sorted(levels) or levels == sorted(levels, reverse=True))
    if b_ordered == False:
        return False
    
    levels = sorted(levels)
    incrs = [abs(levels[x] - levels[x+1]) for x in range(len(levels)-1)]
    
    if max(incrs) > 3 or min(incrs) < 1: return False
    return True

safe_reports = 0
for rep in data.split('\n'):
    if check_report(rep):
        safe_reports +=1
    else:
        for x in range(rep.count(' ')+1):
            if check_report(rep, x):
                safe_reports +=1
                break

print(safe_reports)
# 674
