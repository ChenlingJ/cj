import textwrap, unittest

from hackerrank.lists import parse_commands, run_commands


class TestLists(unittest.TestCase):
    def test_sample_0(self):
        text_in = textwrap.dedent('''
            insert 0 5
            insert 1 10
            insert 0 6
            print
            remove 6
            append 9
            append 1
            sort
            print
            pop
            reverse
            print
        ''').strip()
        # 'insert 0 5'
        # command, *args = ['insert', '0', '5']
        # # command = 'insert'
        # # args = ['0', '5']
        # args = list(map(int, args))
        # pair = (command, args)
        # # pair = ('insert', [0, 5])

        expected = textwrap.dedent('''
            [6, 5, 10]
            [1, 5, 9, 10]
            [9, 5, 1]
        ''').strip()

        actual = '\n'.join(run_commands(parse_commands(text_in.splitlines())))

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
