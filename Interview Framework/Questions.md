# RobinHood:

Robinhood is famous for its referral program. It’s exciting to see our users spreading the word across their friends and family. One thing that is interesting about the program is the network effect it creates. We would like to build a dashboard to track the status of the program. Specifically, we would like to learn about how people refer others through the chain of referral.

For the purpose of this question, we consider that a person refers all other people down the referral chain. For example, A refers B, C, and D in a referral chain of A -> B -> C -> D. Please build a leaderboard for the top 3 users who have the most referred users along with the referral count.

Referral rules:

A user can only be referred once.
Once the user is on the RH platform, he/she cannot be referred by other users. For example: if A refers B, no other user can refer A or B since both of them are on the RH platform.
Referrals in the input will appear in the order they were made.
Leaderboard rules:

The user must have at least 1 referral count to be on the leaderboard.
The leaderboard contains at most 3 users.
The list should be sorted by the referral count in descending order.
If there are users with the same referral count, break the ties by the alphabetical order of the user name.
Input

rh_users = ["A", "B", "C"]
| | |
v v v
new_users = ["B", "C", "D"]

{a: 3, b:2, c:1}

# Reflections

- Should've not printed stuff
- should've seen what I was doing in essence - i.e. sorted I was making rookie mistakes like using name instead of item
- Should've seen what was the expected result and solve it further for the print statement
- I did solve the problem though and got it right to a decent extent

# Meta:

Meta:

"""

      2
     / \
    3   4

/ \
 1 5

231 + 235 + 24 = 490
231 + 2353 + 24 --

Clarifying:
+ve
1 - 9
always binary tree
always solution

"""

class sumDigitTree():
def dfs(self, root, path):

        path = path* 10 + root.val

        if not root.left and root.right:
            self.ans += path
            return

        if root.left:
            self.dfs(root.left, path)

        if root.right:
            self.dfs(roo.right, path)


    def digitSum(self, root):
        self.ans = 0
        self.dfs(root, 0)

        return ans

"""

"aabbaab" -> ["a" "a" "a" "a" "b" "b" "b" "aa" "aa" "bb" "aabbaa" "baab" "abba"]

"abba" - 4, i = 0-2

# ["a", "b", "b", "a", "bb", "abba"]

# Clarifying

# all are lowercase

# all are english characters

# null value could be passed - []

"""

# Space Complexity: size n string

```
class palindromeCombinations():
def checkPal(self, s, left, right):
while left >= 0 and right < len(s) and s[left] == s[right]:
self.res.append(s[left:right+1])
left -= 1
right += 1

    def combination(self, s):
        if not s:
            return []

        self.res = []

        for i in range(len(s)):
            odd = self.checkPal(s, i, i)
            even = self.checkPal(s, i, i+1)

        return self.res

```

# Reflection:

- Space and Time complexity issues
- being a bit more clear with explanation
- Global Variable √
