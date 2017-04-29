

def checkIfNeedToBuild(remainJobs, timeToBuild, currentRobots):
    if currentRobots == 1:
        time = remainJobs
        if time <= timeToBuild:
            return False
        else:
            return True

    notBuildV = currentRobots
    notBuildTime = remainJobs/currentRobots
    if remainJobs%currentRobots != 0:
        notBuildTime += 1
    buildV = currentRobots - 1 + notBuildTime/timeToBuild
    if (notBuildV >= buildV):
        return False
    else:
        return True

def main(remainJobs, timeToBuild):
    currentRobots = 1

    time = 0


    while remainJobs != 0:
        if checkIfNeedToBuild(remainJobs, timeToBuild, currentRobots):
            time += timeToBuild
            remainJobs = remainJobs - (currentRobots-1)*timeToBuild
            currentRobots += 1
        else:
            time = time + remainJobs/currentRobots
            if remainJobs%currentRobots != 0:
                time += 1
            remainJobs = 0
    print time

if __name__ == "__main__":
    # main(10, 2)

    while True:
        try:
            (x, y) = (int(x) for x in raw_input().split())
            main(x, y)
        except EOFError:
            break