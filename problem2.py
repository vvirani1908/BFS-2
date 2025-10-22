# Time Complexity : O(N)         # We visit each node once using BFS
# Space Complexity : O(N)        # Queue can hold up to all nodes at one level
# Did this code successfully run on Leetcode : Yes
# Three line explanation of solution in plain english :
# -> We do a level-order traversal (BFS) of the binary tree.
# -> If x and y appear on the same level but are not siblings, they are cousins.
# -> If only one appears in a level, they can’t be cousins.

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        # Queue for level order traversal
        q = deque()
        q.append(root)

        # Continue until queue is empty
        while q:
            size = len(q)
            x_found = False
            y_found = False

            # Process all nodes at the current level
            for i in range(size):
                curr = q.popleft()

                # If current node has both left and right child
                # check if they are x and y (siblings)
                if curr.left and curr.right:
                    if (curr.left.val == x and curr.right.val == y) or \
                       (curr.left.val == y and curr.right.val == x):
                        # x and y are siblings, not cousins
                        return False

                # Mark if we found x or y at this level
                if curr.val == x:
                    x_found = True
                if curr.val == y:
                    y_found = True

                # Add children to the queue for next level
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

            # After finishing this level
            # If both x and y are found → they are cousins
            if x_found and y_found:
                return True
            # If only one is found → they can’t be cousins
            if x_found or y_found:
                return False

        # If traversal finishes and we didn’t return yet → not cousins
        return False
