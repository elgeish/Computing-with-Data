sm = 0
# repeat for 100 iteration, with num taking values 1:100
for (num in seq(1, 100, by = 1)) {
    sm = sm + num
}
sm  # same as sum(1:100)

repeat {
    sm = sm - num
    num = num - 1
    if (sm == 0) break  # if sm == 0 then stop the loop
}
sm

a = 1
b = 10
# continue the loop as long as b > a
while (b > a) {
    sm = sm + 1
    a = a + 1
    b = b - 1
}
sm
