#
# [32] Longest Valid Parentheses
#
# https://leetcode.com/problems/longest-valid-parentheses/description/
#
# algorithms
# Hard (23.36%)
# Total Accepted:    130.5K
# Total Submissions: 558.4K
# Testcase Example:  '"(()"'
#
# Given a string containing just the characters '(' and ')', find the length of
# the longest valid (well-formed) parentheses substring.
#
# Example 1:
#
#
# Input: "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()"
#
#
# Example 2:
#
#
# Input: ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()"
#
#
#


class BruteForceSolution:
    def num_valid(self, s):
        stack = []
        count = 0
        best_count = 0

        for c in s:
            if c == '(':
                stack.append(c)
                count += 1
            else:
                # unbalanced right
                if not stack:
                    return best_count
                stack.pop()
                count += 1
                if not stack:
                    best_count = max(best_count, count)
        # unbalanced left
        if stack:
            return best_count
        return best_count

    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for i in range(len(s)):
            count = max(count, self.num_valid(s[i:]))
        return count


class MyWrongSolution:
    def get_ridge(self, s, start):
        r = [0] * (len(s) + 1)
        r[0] = start
        level = start
        for i, c in enumerate(s):
            level += 1 if c == '(' else -1
            r[i+1] = level
        return r

    def add(self, i, ridge, direction, rev_direction, pos):
        # is there room for the next item?
        if not (0 <= i+direction < len(ridge)):
            # print('next out of bound', i, direction)
            return None

        # are we going down? if so, don't bother
        # next in current direction should be == current + 1
        this_level = ridge[i]
        next_level = ridge[i + direction]
        try:
            if this_level + 1 != next_level:
                # print('skip as going down', i, direction)
                # print(this_level, next_level)
                return None
        except IndexError:
            # print(ridge)
            # print(i, direction)
            raise

        # pos contains the following keys:
        #   (level, direction)
        # it only stores entries that go up
        # remember current position
        if (this_level, direction) not in pos and direction == 1:
            pos[(this_level, direction)] = i
            print('added', this_level, direction, i)

        # is complement position present?
        if (this_level, rev_direction) not in pos:
            return None

        other_i = pos[(this_level, rev_direction)]
        if other_i >= i:
            return None

        result = max(i, other_i) - min(i, other_i)
        print('found at', other_i, this_level, rev_direction, '=', result)
        return result

    def longestValidParentheses(self, s):
        # s = ')' + s
        ridge = self.get_ridge(s, 0)
        print('      ', ', '.join(s))
        print('ridge', ridge)
        # left, right = 0, len(s) - 1
        pos = dict()

        for i in range(len(ridge)):
            if i+1 < len(ridge):
                level, next_level = ridge[i], ridge[i+1]
                if level + 1 == next_level and level not in pos:
                    print('go up right at', i, 'level', level)
                    pos[level] = i

        dist = 0
        for i in range(len(ridge)-1, -1, -1):
            if i > 0:
                level, next_level = ridge[i], ridge[i-1]
                if level + 1 == next_level and level in pos:
                    other_i = pos[level]
                    current_dist = i - other_i
                    if current_dist > 0:
                        dist = max(dist, current_dist)
                        print('go up left at', i, 'level',
                              level, 'new dist', dist)
                    # if i > other_i:
                    #     print('go up left at', i, 'level', level)
                    # pos[level] = i

        # for i in range(len(s)):
        #     self.add(i, ridge, 1, -1, pos)

        # for i in range(len(s)-1, -1, -1):
        #     current_dist = self.add(i, ridge, -1, 1, pos)
        #     if current_dist is not None:
        #         dist = max(dist, current_dist)

        # while left < right:
        #     dist = self.add(left, ridge, 1, -1, pos)
        #     if dist is not None:
        #         return dist
        #     left += 1
        #     dist = self.add(right, ridge, -1, 1, pos)
        #     if dist is not None:
        #         return dist
        #     right -= 1

        return dist


class Solution:
    def longestValidParentheses(self, s):
        best = 0
        dp = [0] * len(s)
        for i in range(1, len(s)):
            if s[i] == ')' and s[i-1] == '(':
                prev = dp[i-2] if i >= 2 else 0
                dp[i] = prev + 2
            elif s[i] == ')' and s[i-1] == ')':
                if i - dp[i-1] > 0 and s[i - 1 - dp[i-1]] == '(':
                    index = i - 2 - dp[i-1]
                    c = dp[index] if index >= 0 else 0
                    dp[i] = dp[i-1] + 2 + c
            best = max(best, dp[i])
        return best


def assert_eq(actual, expected):
    if actual != expected:
        raise AssertionError('expected: %s, actual: %s' % (expected, actual))


def test(input_, output):
    assert_eq(Solution().longestValidParentheses(input_), output)


if __name__ == '__main__':
    test('(())()(()((', 6)
    test('))))((()((', 2)
    test('()(()', 2)
    test('(()', 2)
    test('(()))())(', 4)
    test(')()())', 4)
    test('', 0)
    test('()', 2)
