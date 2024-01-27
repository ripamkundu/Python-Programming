def operation_1():
    a=5
    b=8.3365
    c=a+b
    m=a*b
    d=a/b
    s=a-b
    print("addition=",round(c,1))
    print("multiplication=",round(m,1))
    print("division",round(d,1))
    print("substruction=",round(s,1))
def operation_2():
    name="Subhapriyo Ghosh"
    a="21"
    stream="EE"
    roll_no="02"
    college="MIT"
    year="3rd"
    here_is="name -> {0},age is -> {1},stream is -> {2},roll no is -> {3},studying in -> {4},year is -> {5}"
    print(here_is.format(name,a,stream,roll_no,college,year))
operation_1()
operation_2()