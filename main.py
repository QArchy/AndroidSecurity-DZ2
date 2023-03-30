import itertools
import hashlib


numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
lowercase = [chr(i) for i in range(ord('a'), ord('z') + 1)]
uppercase = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
codes = ["f74ab58bf14d5daa76f3ac45955f992a", "1fe4d3175df6017982ba4a071f6b1b60", "31f71290797f7df507f8ba6c1d4c54ff",
         "45f7fe6c6eb37d10075985b67abf34ca", "09a21d6a244ee096261173c718883342", "1fbcc6c3832577fda3fc0f622111b0f1",
         "874c88009580ddb6d1f0b1ec933e642f", "1f0d0ea72895aeb0ae34f7e5b442721b", "c48e2ebd699299655bddf117cd0118fe",
         "dab90b6d1527f2ae3c4059a6f719e821", "3ac37da614bee6ec2e7e9ad6f5852dd8", "4b4b55dbbff14347656aa47ba7775d3e",
         "1927811792f88a3bca7096621f69e771", "073c7095bd87360317d30e4b2e91ccf7", "3eb34357ddb30096e79cb5ac8323ad35",
         "5efa3f5a222de026c57b4b48808d1ae1", "ebdefbd752e87462fa34c85cb92e3e85", "a7b05d3cd60d38ee001816d7672770d1",
         "b61dc4ff0c47c1e8cb662691fb3a2f16", "29a058aa9e2ca45f66988373ba1951aa", "46b23925b8c2ea830448fe4e892b10be",
         "8c0936fad85e8183a95c0cef97e52f97", "76e362d7f1928a7446e814298c49d3fc", "36327a78cb1882b950347b7af99f2bd2",
         "0b675ac8c7808eb306df102f9956dcb4", "e0361cd6fd8ea6f4096483a39137263c", "da028029f16562e73501896134f89b64",
         "0279c0c44fc42aa3345e0e724a0632b9", "0477e4f96b91f8ebeffec0bd1669ff71", "f97371214734321537451da5a3491f84",
         "3490d4344fe6a8c9f16ec61d8a7cc250", "b66ebe00e0f8da9b3158ab868c26253b", "448a88754a0dd106a489a9a677c00b66",
         "844e735ce6f6ecc796949b57f722710b", "c53f1568bd4f072f2ba9e836c7388367", "58dfba14a56910f8e4834d727b75b8bc",
         "32fcf126fae80250209ed9c027d9a907", "2c69bba613a4f0bc090202fb637c102b", "115e1efd1692bf685e2e0f6c2b3c10a6",
         "197f0c0d65dc6097f3b1c4506e4fe4ea", "0253b601bccb3060eb2d22bb671ac465", "9bfafd774ba45323e67447826de1b75c",
         "cf0dbc67cff9060eb7fb7f887a8f2ca6", "836473307fa2a6dd0897f932dd53984e", "6faaadac456112c9f6b8d4174cfbb81b",
         "6b837eb46bf851b2a1b7db6ae4f4b15a", "bd4e7dea82c6ad186dda296fce855ab9", "3124a35362e14564f92b807ff4510240",
         "e6a6a3edeabbbb38e0459d3757b90498", "6e28c629a7750c74e42fdf7b5b9e6f64", "118458796bbb3c768ad301108f21c35d"]


def calcPassword(id):
    permutations = [''.join(p) for p in itertools.product(numbers + lowercase + uppercase, repeat=4)]
    prefixed_permutations = ["MySecretNuberIs_" + s for s in permutations]
    encoded_prefixed_permutations = [s.encode('utf-8') for s in prefixed_permutations]
    digest = [hashlib.md5(s).hexdigest() for s in encoded_prefixed_permutations]
    if codes[id - 1] in digest:
        print(prefixed_permutations[digest.index(codes[id - 1])])


calcPassword(15)
