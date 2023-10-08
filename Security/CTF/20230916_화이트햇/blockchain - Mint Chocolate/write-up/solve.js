const hre = require("hardhat");

async function main() {
  const setup = await hre.ethers.getContractAt(
    [
      {
        inputs: [],
        name: "TARGET",
        outputs: [
          {
            type: "address",
          },
        ],
        stateMutability: "view",
        type: "function",
      },
    ],
    "0xeCf916f52dF5e43c9c2849962F81624DaE20D728"
  );

  const mintChoAddr = await setup.TARGET();

  const minCho = await hre.ethers.getContractAt(
    [
      {
        inputs: [],
        name: "totalSupply",
        outputs: [
          {
            internalType: "uint256",
            name: "",
            type: "uint256",
          },
        ],
        stateMutability: "view",
        type: "function",
      },
    ],
    mintChoAddr
  );

  const exploit = await hre.ethers.deployContract("ExploitContract", [mintChoAddr]);
  await exploit.waitForDeployment()
  const gasLimit = hre.ethers.parseUnits('100000', 'wei');

  console.log(await exploit.run());

  // console.log(await exploit.counter())
  console.log(await minCho.totalSupply())
}

// We recommend this pattern to be able to use async/await everywhere
// and properly handle errors.
main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
