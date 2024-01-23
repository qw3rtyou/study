# Baby-rev
- 리버싱을 수작업이 아닌 약간의 자동화된 방식(debugger script, symbolic execution)을 요구하는 문제

# 문제 풀이(Dob6y님 풀이)
- 출제자 풀이임
- 20240122 솔직히 아직 이해 못했음 - 이해하고 첨삭 바람

```python
import angr
import claripy

import sys

import logging

def main(argv):
    path_to_binary = argv[1]  # :string
    project = angr.Project(path_to_binary)

    start_address = 0x401286

    result = ""

    for rnd in range(0, 16):
        flag = claripy.BVS('flag', 32)
        rndv = claripy.BVV(rnd, 32)


        initial_state = project.factory.call_state(
        start_address,
        flag,
        rndv
        )

        simulation = project.factory.simgr(initial_state)

        good_address = 0x409535

        simulation.explore(find=good_address)

        if simulation.found:
            if len(simulation.found) > 1:
                print("zz")
                print(len(simulation.found))
                exit(0)

            solution_state = simulation.found[0]

            for i in range(3, -1, -1):
                solution_state.solver.add((flag >> (i * 8) & 0xff) >= 0x20)
                solution_state.solver.add((flag >> (i * 8) & 0xff) < 0x7f)

            print("[+] Round {} : {}".format(rnd, solution_state.solver.eval(flag, cast_to=bytes)))
            result += solution_state.solver.eval(flag, cast_to=bytes).decode()
        else:
            raise Exception('Could not find the solution')

    print(result)

if __name__ == '__main__':
    main(sys.argv)

```