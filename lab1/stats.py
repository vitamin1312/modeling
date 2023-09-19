import seaborn as sns
from matplotlib import pyplot as plt
from tqdm import tqdm
import math
from utils import in_interval


def lemers_method(x0, a=16807, module=2_147_483_647, size=1000):
    nums = [x0 / module]

    for _ in tqdm(range(size - 1)):
        x1 = a * x0 % module
        val = x1 / module

        if val in nums:
            print('Generated value in random numbers')
            return nums

        nums.append(val)
        x0 = x1

    return nums


def plot_hist_F(nums, hist_name, F_name):
    sns.histplot(data=nums, stat='density')
    plt.savefig(hist_name)
    plt.clf()
    sns.displot(data=nums, kind="ecdf")
    plt.savefig(F_name)
    plt.clf()


def chi_square(nums):
    size = len(nums)
    m = int(size / 10)
    h = 1 / m
    x = [h*i for i in range(m + 1)]
    n = [in_interval(nums, x[i], x[i+1]) for i in range(m)]
    return m / size * sum(map(lambda elem: elem**2, n)) - size


def kolmogorov(nums):
    nums = list(sorted(nums))
    size = len(nums)
    dF = 1 / size
    F = [dF*i for i in range(size+1)]
    return size**0.5 * max(max([F[i] - nums[i], F[i + 1] - nums[i]]) for i in range(size))


def series(nums):

    nums_ord = list(sorted(nums))
    size = len(nums)

    if size % 2 == 0:
        med_idx = int((size + 1) / 2)
        med = nums_ord[med_idx]
        nums.pop(med_idx)
    else:
        med_idx_f = math.floor(size/2)
        med_idx_c = math.ceil(size / 2)
        med = (nums_ord[med_idx_f] + nums_ord[med_idx_c])

    sign = [elem > med for elem in nums]  # True is +; False is -

    nps, nms = 0, 0
    previous_s = sign[0]

    for s in sign[1:]:

        if s != previous_s and previous_s:
            nms += 1
        elif s != previous_s and not previous_s:
            nps += 1

        previous_s = s

    r = nms + nps
    nm = sum(1 for s in sign if not s)
    np = sum(1 for s in sign if s)

    mu = 2*np*nm / size + 1
    sigma_sq = 2*np*nm*(2*np*nm - size) / ((size**2)*(size - 1))
    sigma = sigma_sq**0.5

    return (r - mu) / sigma
