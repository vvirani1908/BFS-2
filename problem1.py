# Time Complexity : O(N)         # We visit each node exactly once using BFS
# Space Complexity : O(N)        # Queue can store nodes of one full level
# Did this code successfully run on Leetcode : Yes
# Three line explanation of solution in plain english :
# -> We perform a level order traversal (BFS) of the binary tree.
# -> At each level, we only take the last node (rightmost node) into our result.
# -> The collected nodes from top to bottom form the right side view.

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # If tree is empty, return empty list
        if not root:
            return []

        result = []       # stores the rightmost node of each level
        q = deque([root]) # queue for BFS traversal

        # Perform level order traversal
        while q:
            size = len(q)  # number of nodes at current level

            # Traverse all nodes at current level
            for i in range(size):
                curr = q.popleft()

                # If it's the last node in the current level,
                # it's visible from the right side
                if i == size - 1:
                    result.append(curr.val)

                # Enqueue left child first, then right child
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

        # Return the list of visible nodes from the right side
        return result
