package linkedlist

/* The types needed for the linked list */

type node struct {
        value string
        next *node
}

type List struct {
        head *node
        length int
}
