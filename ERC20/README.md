ERC20



```solidity
mapping(string => uint256) public userToken;
可以传入string类型的userId来获取其代币数量


1.function AddToken(string memory userId,uint256 value) public onlyOwner
给userId用户增加多少币
2.function SubToken(string memory userId,uint256 value) public onlyOwner
给userId用户减少多少币
require(userToken[userId] >= value,"Balance is not engouth!");有余额判断
3.function TokenZere(string memory userId) public onlyOwner{
把userId用户币归零
4.function WithdrawToAddress(string memory userId,address useraddresss,uint256 value) public onlyOwner
把userId的value数量的币转到链上useraddress地址
5.function TransferToUser(string memory userIdA, string memory userIdB,uint256 value) public onlyOwner
把userIdA的value数量的币转给userIdB用户
```



