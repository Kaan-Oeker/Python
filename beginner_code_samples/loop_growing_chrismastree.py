class loopGrowingChrismastree():
    def __init__(self) -> None:
        pass
        
    def buildChrismastree(loop_count):
        z_axis = loop_count - 1
        x_axis = 1
        for i in range(loop_count):
            print(' ' * z_axis + '+' * x_axis + ' ' * z_axis)
            x_axis += 2
            z_axis -= 1

loopGrowingChrismastree.buildChrismastree(5)