```solidity
function AddVideo(string memory userId, string memory vlogId) onlyOwner public
require(Video_info[VIDEO_userId_vlogId].createtime!=0,"It has been stored")
增加video信息


function AddTort(string memory userId,string memory vlogId) onlyOwner public returns(uint)
require(Video_tort[TORT_vlogId_userId].createtime == 0,"It has been a Tort");
require(balanceOf(msg.sender,Video_info[VIDEO_userId_vlogId].createtime)!=0,"It is not a video");
增加侵权信息


function AddIllegle(string memory userId,string memory vlogId,string memory kind) onlyOwner public
增加违规信息
require(Illegle_video[ILLEGEL_userId_vlogId].illegelTime == 0,"It has been a ILLEGEL");
require(Video_info[ILLEGEL_userId_vlogId].createtime!=0,"It is not a video");





  mapping(string => Video) public Video_info;
  mapping(string => Video) public Video_tort;
  mapping(string => Illegle_videio) public Illegle_video;
    struct Video{
    string userId;
    uint createtime;
    string vlogId;
  }
  struct Illegle_videio{
    string userId;
    string kind;
    uint illegelTime;
    uint createtime;  
  }
```

