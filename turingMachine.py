class TuringMachine:
    def __init__(self, tape, blank_symbol="□"):
        self.tape = list(tape)
        self.blank_symbol = blank_symbol
        self.head_position = 0
        self.current_state = 'q0'
        self.transition_function = {
            ('q0', 'a'): ('a', 'R', 'q1'),
            ('q1', 'b'): ('b', 'R', 'q2'),
            ('q2', 'b'): ('b', 'R', 'q3'),
            ('q3', 'a'): ('a', 'R', 'q1'),
            ('q3', self.blank_symbol): (self.blank_symbol, 'R', 'q4'),
        }
    
    def step(self):
        symbol_under_head = self.tape[self.head_position]
        if (self.current_state, symbol_under_head) in self.transition_function:
            write_symbol, direction, next_state = self.transition_function[(self.current_state, symbol_under_head)]
            self.tape[self.head_position] = write_symbol
            self.current_state = next_state
            if direction == 'R':
                self.head_position += 1
                if self.head_position >= len(self.tape):
                    self.tape.append(self.blank_symbol)
            elif direction == 'L':
                if self.head_position > 0:
                    self.head_position -= 1
        else:
            self.current_state = 'REJECTED'

    def run(self):
        while self.current_state not in ['q4', 'REJECTED']:
            self.step()

        return self.current_state == 'q4'