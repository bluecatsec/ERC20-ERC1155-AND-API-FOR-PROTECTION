pragma solidity 0.8.1;

import "./ERC1155.sol";
import "./string.sol";

contract Video is ERC1155 {

  event _AddVideo(string _userId, string _vlogId);
  event _AddTort(string _userId,string _vlogId);
  event _AddIllegle(string _userId,string _vlogId,string _kind);

  using strings for *;
  address public owner;

  modifier onlyOwner() {
        require(msg.sender == owner, "only owner can call this");
        _;
    }

  constructor() ERC1155("") public {
    owner = msg.sender;
  }

  function stringToBytes32(string memory source) internal returns(bytes memory result){
        assembly{
            result := mload(add(source,32))
        }
  }

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

    struct Tort_Video{
    string userId;
    uint createtime;
    string vlogId;
    string torted_userId;
  }

  mapping(string => Video) public Video_info;
  mapping(string => Tort_Video) public Video_tort;
  mapping(string => Illegle_videio) public Illegle_video;

  function AddVideo(string memory userId, string memory vlogId) onlyOwner public {
    string memory VIDEO_userId_vlogId = userId.toSlice().concat(vlogId.toSlice());
    Video_info[VIDEO_userId_vlogId] = Video(userId,block.timestamp,vlogId);
    bytes memory data_tmp = stringToBytes32(VIDEO_userId_vlogId);
    _mint(msg.sender,block.timestamp,1,data_tmp);
    emit _AddVideo(userId,vlogId);
  }

  function AddTort(string memory userId,string memory torted_userId,string memory vlogId) onlyOwner public returns(uint){
    string memory TORT_vlogId_userId = vlogId.toSlice().concat(userId.toSlice());
    require(Video_tort[TORT_vlogId_userId].createtime == 0,"It has been a Tort");
    Video_tort[TORT_vlogId_userId] = Tort_Video(userId,block.timestamp,vlogId,torted_userId);
    string memory VIDEO_userId_vlogId = userId.toSlice().concat(vlogId.toSlice());
    require(balanceOf(msg.sender,Video_info[VIDEO_userId_vlogId].createtime)!=0,"It is not a video");
    emit _AddTort(userId,vlogId);
    return Video_info[VIDEO_userId_vlogId].createtime;
  }

  function AddIllegle(string memory userId,string memory vlogId,string memory kind) onlyOwner public{
    string memory ILLEGEL_userId_vlogId = userId.toSlice().concat(vlogId.toSlice());
    require(Illegle_video[ILLEGEL_userId_vlogId].illegelTime == 0,"It has been a ILLEGEL");
    Illegle_video[ILLEGEL_userId_vlogId] = Illegle_videio(userId,kind,block.timestamp,Video_info[ILLEGEL_userId_vlogId].createtime);
    emit _AddIllegle(userId,vlogId,kind);
  }

}