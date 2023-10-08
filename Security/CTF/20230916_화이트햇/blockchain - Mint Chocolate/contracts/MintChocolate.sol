pragma solidity ^0.8.13;
import "./token/ERC721.sol";

contract MintChocolate is ERC721 {
    bool public minted;
    uint256 public counter;

    constructor() ERC721("MintChocolate", "MC") {}
    function mint(uint256 amount) external {
        require(!minted, "No more mint");
        require(amount <= 10, "mint cap reached");

        for(uint256 i = 0; i < amount;) {
            _safeMint(msg.sender, counter++);
            
            unchecked {
                ++i;
            }
        }
        minted = true;
    }

    function goldenTicket() view external returns(bool) {
        return totalSupply() >= 100 ? true : false;
    }
}
