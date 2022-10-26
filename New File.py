s="ксти"
for x1 in s:
    for x2 in s:
        for x3 in s:
            for x4 in s:
                itog=x1+"а"+x2+x3+x4
                if(itog.count("к")==1 and itog.count("и")==1 and  itog.count("с")==1 and itog.count("т")==1):
                    print(itog)
