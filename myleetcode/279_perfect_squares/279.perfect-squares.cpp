/*
 * @lc app=leetcode id=279 lang=cpp
 *
 * [279] Perfect Squares
 *
 * https://leetcode.com/problems/perfect-squares/description/
 *
 * algorithms
 * Medium (40.27%)
 * Total Accepted:    175.9K
 * Total Submissions: 422.9K
 * Testcase Example:  '12'
 *
 * Given a positive integer n, find the least number of perfect square numbers
 * (for example, 1, 4, 9, 16, ...) which sum to n.
 *
 * Example 1:
 *
 *
 * Input: n = 12
 * Output: 3
 * Explanation: 12 = 4 + 4 + 4.
 *
 * Example 2:
 *
 *
 * Input: n = 13
 * Output: 2
 * Explanation: 13 = 4 + 9.
 */
#include <algorithm>
#include <climits>
#include <stdexcept>
#include <string>
#include <vector>

class Solution {
public:
    int numSquares(int n)
    {
        std::vector<int> dp(n + 1, INT_MAX);
        dp[0] = 0;

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j * j <= i; j++) {
                dp[i] = std::min(dp[i], dp[i - j * j] + 1);
            }
        }

        return dp[n];
    }
};

void test(int input, int expectedOutput)
{
    Solution solution = Solution();
    int actual = solution.numSquares(input);
    if (actual != expectedOutput) {
        throw std::runtime_error(
            std::string("FAILED, actual = ") + std::to_string(actual));
    }
}

// int main()
// {
//     test(12, 3);
//     test(13, 2);
//     test(40, 2);
// }
