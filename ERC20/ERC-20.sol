// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./ERC20.sol";


contract TokenERC20 is ERC20 {

    address public owner;

    modifier onlyOwner() {
        require(msg.sender == owner, "only owner can call this");
        _;
    }

    constructor(uint256 initialSupply_, string memory name_, string memory symbol_) ERC20(name_, symbol_) payable {
        owner = msg.sender;
        _mint(msg.sender, initialSupply_);
    }
    
    mapping(string => uint256) public userToken;

    function AddToken(string memory userId,uint256 value) public onlyOwner {
        userToken[userId]+=value;
    } 

    function SubToken(string memory userId,uint256 value) public onlyOwner {
        require(userToken[userId] >= value,"Balance is not engouth!");
        userToken[userId]-=value;
    } 

    function TokenZere(string memory userId) public onlyOwner{
        userToken[userId] = 0;
    }

    function WithdrawToAddress(string memory userId,address useraddresss,uint256 value) public onlyOwner{
        require(userToken[userId] >= value,"Balance is not enough!");
        userToken[userId] -= value;
        transfer(useraddresss,value);
    }

    function TransferToUser(string memory userIdA, string memory userIdB,uint256 value) public onlyOwner{
         require(userToken[userIdA] >= value,"Balance is not enough!");
         userToken[userIdA] -=value;
         userToken[userIdB] +=value;
    }

}