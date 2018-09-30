# Example 1 - sample 3 times from the values [1, 2, 3, 4] without replacements
sampled_row_indices = sample(1:4, 3, replace = FALSE)
print(sampled_row_indices)

# Example 2 - sampled rows
d = array(data = seq(1, 20, length.out = 20), dim = c(4, 5))
d_sampled = d[sampled_row_indices, ]
print(d_sampled)

# Example 3 - partition an array into two new arrays of sizes 75% and 25%
d = array(data = seq(1, 20, length.out = 20), dim = c(4, 5))
print(d)
rand_perm = sample(4, 4)
first_set_of_indices = rand_perm[1:floor(4 * .75)]
second_set_of_indices = rand_perm[(floor(4 * .75) + 1):4]
print(d[first_set_of_indices, ])
print(d[second_set_of_indices, ])

# Example 4 - shuffling
d = array(data = seq(1, 20, length.out = 20), dim = c(4, 5))
print(d)
d_shuffled = d[sample(4, 4), ]
print(d_shuffled)
