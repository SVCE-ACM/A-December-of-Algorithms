using System;

class Node {
	/* Fields */
        private int value;
        private Node next;
        private Node down;

        /*Constructors*/
        public Node () {
                value = 0;
                next = null;
                down = null;
        }

                public Node (Node node) {
                        this.value = node.value;
                        this.next = node.next;
                        this.down = node.down;
                }

                /* Properties */
                public Node Next {
                        get { return next; }
                }

                public Node Down {
                        get { return down; }
                }
}


class LinkedList {

	class Node {
		/* Fields */
		private int value;
		private Node next;
		private Node down;

		/*Constructors*/
		public Node () {
			value = 0;
			next = null;
			down = null;
		}

		public Node (Node node) {
			this.value = node.value;
			this.next = node.next;
			this.down = node.down;
		}

		/* Properties */
		public Node Next {
			get { return next; }
		}

		public Node Down {
			get { return down; }
		}
	}
