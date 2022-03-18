var = 17
var_right = var >> 1 #shifts a value to the right (for binary divide(//) by two)
# 17 (0b10001) turns into 8 (0b1000) note the last bit is lost (17 // 2 = 8)
var_left = var << 2 #shifts a value to the left by two (binary: multiply by two)
# 17(0b10001) turns into 68(0b1000100) note (17 * 2 * 2 = 68)
print(var, var_left, var_right)
