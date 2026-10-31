# Latest papers for 程旭丽

Updated: 2026-10-31T03:48:34.870689+00:00
Window: last 14 days

## Notes

- arXiv query failed for 机器学习分子动力学模拟与热力学性质: The read operation timed out
- 机器学习分子动力学模拟与热力学性质 kept previous papers because the current query returned 0 results.
- arXiv query failed for 凝聚态物理强关联体系和多铁性质: The read operation timed out
- 凝聚态物理强关联体系和多铁性质 kept previous papers because the current query returned 0 results.

## 机器学习分子动力学模拟与热力学性质

### 1. Nitrogen vacancy cluster-mediated ferroelectric domain growth in wurtzite AlN

- Source: arXiv
- Date: 2026-10-22T10:56:32Z
- Venue: cond-mat.mtrl-sci
- Authors: Zijian Zhou, Kan-Hao Xue, Ziqi Pang, Heng Yu, Shanzhong Xie, Hang Liu
- Link: https://arxiv.org/abs/2610.31084v1
- Score: 12.0
- Match: 摘要匹配 deep potential molecular dynamics; 最近 3 天发布

**中文摘要：** 氮化铝基铁电体结合了高剩余极化、热稳定性、弱尺寸效应、宽带隙和后端工艺兼容性，使其有望用于高密度非易失性存储器。然而，它们的高矫顽场（$E_\mathrm{c}$）和不明确的偏振切换机制限制了进一步的应用。理论预测表明沿极轴优先反向域生长，而实验显示近各向同性生长或垂直于该轴的优先生长。 在这里，我们结合密度泛函理论、深势分子动力学和实验表征来确定氮空位 ($V_\mathrm{N}$) 如何调节域生长和 $E_\mathrm{c}$。在理想晶体中，沿极轴的强晶格耦合驱动沿该方向的择优生长。 $V_\mathrm{N}$ 局部减弱这种耦合并促进极化成核。 $V_\mathrm{N}$ 的空间分布和空位引起的切换的时间序列共同决定了反向域生长的方向和形态。 我们进一步表明，钪掺杂促进 $V_\mathrm{N}$ 的形成，从而增强缺陷介导的成核并减少 $E_\mathrm{c}$。这些发现建立了控制薄膜畴生长动力学和宏观$E_\mathrm{c}$的多尺度机制，将实验观察与理想晶体模拟相协调，并为低电压、可靠和可扩展的铁电器件提供缺陷工程原理。
**讨论重点：** 氮化铝基铁电体结合了高剩余极化、热稳定性、弱尺寸效应、宽带隙和后端工艺兼容性，使其有望用于高密度非易失性存储器。然而，它们的高矫顽场（$E_\mathrm{c}$）和不明确的偏振切换机制限制了进一步的应用。 结合关键词看，阅读时应重点关注深度势分子动力学相关的极化翻转、磁电耦合、自旋-晶格耦合以及多铁序参量之间的相互制约。

### 2. Concentration-Dependent Speciation in ZnCl2 Electrolyte Solutions: Transferability of Machine-Learning Interatomic Potentials and Speciation Sensitivity of EXAFS

- Source: arXiv
- Date: 2026-10-21T22:46:57Z
- Venue: physics.chem-ph
- Authors: Junhan Chen, Luke D. Gibson, Nadia N. Intan, Darren M Driscoll, Mahalingam Balasubramanian, John L. Fulton
- Link: https://arxiv.org/abs/2610.30513v1
- Score: 11.0
- Match: 摘要匹配 DeepMD; 最近 3 天发布

**中文摘要：** 预测浓电解质中的形态需要准确的离子相互作用和对缓慢相互转换的配位环境进行充分采样。我们使用机器学习原子间势将 Zn K 边扩展 X 射线吸收精细结构 (EXAFS) 测量与长时标分子动力学 (MD) 相结合，研究从稀释条件到 30 m 的 ZnCl2 水溶液。我们训练基于 revPBE 的 DeepMD 模型，其中包含或排除含 Zn 对的 D3 校正，并将它们与 DPMD-SCAN、经典 MD (CMD) 和 MACE-MATPES-r2SCAN 进行比较。 EXAFS 计算以水合和氯化物配位 Zn 参考络合物为基准，然后应用于 MD 系综以及 Zn-Cl 配位自由能分析。增加浓度会减少八面体配位，用氯化物代替水，并促进氯化物桥联。所有三个 DeepMD 模型在 3 m 处均产生类似的 EXAFS，但 DPMD-SCAN 显示出更大的跨浓度可转移性，再现了测量的光谱趋势、混合 ZnCl2/LiCl 光谱的关键特征以及与其他研究一致的八面体分数。 DFT 处理强烈影响配位自由能和聚集；排除与 Zn 相关的 D3 修正并不能系统地改善 EXAFS 一致性。 CMD 显示出较大的光谱差异和不太一致的协调趋势。 MACE-MATPES-r2SCAN 在 CMD 的基础上进行了改进，产生的光谱可与 DPMD-SCAN 相媲美，从而提供更一致的一致性和更高的计算效率。 邻域解析分析表明，距离无序和散射路径干扰可以为不同的配位系综产生类似的 EXAFS 特征，这突出表明需要严格采样和系综平均光谱来区分分离的和氯桥 Zn 物种。
**讨论重点：** 我们使用机器学习原子间势将 Zn K 边扩展 X 射线吸收精细结构 (EXAFS) 测量与长时标分子动力学 (MD) 相结合，研究从稀释条件到 30 m 的 ZnCl2 水溶液。我们训练基于 revPBE 的 DeepMD 模型，其中包含或排除含 Zn 对的 D3 校正，并将它们与 DPMD-SCAN、经典 MD (CMD) 和 MACE-MATPES-r2SCAN 进行比较。 结合关键词看，阅读时应重点关注DeepMD相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 3. Scalable long-range machine learning interatomic potentials with electrical response for atomistic material modeling

- Source: arXiv
- Date: 2026-10-16T15:44:07Z
- Venue: cond-mat.mtrl-sci, cs.LG
- Authors: Yicheng Chen, Xiaoyun Yu, Hyejeong Song, Xintian Wang, Zihui Li, Zixi Xia
- Link: https://arxiv.org/abs/2610.23643v1
- Score: 10.0
- Match: 标题匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 在电场下对材料进行精确的原子模拟需要在长度尺度上进行长程静电和电响应建模，这超出了传统第一原理方法的范围。然而，这些功能仍然难以与机器学习原子间势（MLIP）的可扩展性相协调。严格的局部模型可以实现高效的空间并行化，但忽略了远程交互，而现有的静电扩展引入了阻碍分布式计算的全局依赖性。 在这里，我们通过分析将长程静电力和玻恩有效电荷（BEC）分离为全局静电计算和学习潜电荷的严格局部导数来克服这一限制。该公式保留了等变 MLIP 的空间可分解性，同时能够跨不同边界条件对能量、力、应力和 BEC 进行分布式评估。 该框架在 \texttt{nvalchemi} 平台上以 DPA4C-LR 的形式实现，可在四个 GPU 上扩展到 520 万个原子，其计算成本约为其短程主干的两倍。经过能量和力的训练，DPA4C-LR 可以准确推断 BEC 并再现水的场相关红外光谱。 我们通过恢复弛豫器 \ce{Pb(Mg_{1/3}Nb_{2/3})O3} 特有的微小极化滞后来进一步证明其功能，该滞后在较小的模拟中被有限尺寸效应所掩盖；预测非晶态 \ce{Li_{0.9}NbO_{0.9}Cl_{4.1}} 中室温场驱动离子电导率为 $6.8 \pm 0.7$~mS/cm；并利用平板校正静电对跨硅/金刚石界面的界面热传输进行建模。
**讨论重点：** 严格的局部模型可以实现高效的空间并行化，但忽略了远程交互，而现有的静电扩展引入了阻碍分布式计算的全局依赖性。该框架在 \texttt{nvalchemi} 平台上以 DPA4C-LR 的形式实现，可在四个 GPU 上扩展到 520 万个原子，其计算成本约为其短程主干的两倍。 结合关键词看，阅读时应重点关注机器学习原子间势相关的第一性原理设置、对称性分析、能带或响应函数计算，以及这些量与可观测物性的对应关系。

### 4. Machine Learning-Assisted Discovery of Carbon-Related Defect Formation Mechanisms in Diamond

- Source: arXiv
- Date: 2026-10-19T12:51:02Z
- Venue: cond-mat.mtrl-sci
- Authors: Grace Huang, Christopher Fivecoat, Xun Xu, Mengen Wang
- Link: https://arxiv.org/abs/2610.26301v1
- Score: 9.0
- Match: 摘要匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 金刚石是固态自旋量子位等功能缺陷的重要主体材料。在通过辐射和随后的热退火产生缺陷的过程中，会产生与碳相关的缺陷，包括空位和填隙，并且可以迁移形成新的缺陷复合体。为了研究这种动力学驱动的过程并揭示中性电荷态双填隙和双空位的形成机制，我们使用密度泛函理论计算生成的小数据集对通用机器学习原子间势进行了微调。 我们获得了单填隙迁移的势垒为 1.84 eV，并发现两个最初分离的单填隙只需克服较低的势垒即可形成双填隙构型。除了训练数据之外，MLIP 还确定了额外的双间隙构型和逐步双空位解离机制的形成途径。这些结果揭示了迁移辅助缺陷复合体形成机制，并证明了有针对性的 MLIP 训练如何识别反应途径。
**讨论重点：** 为了研究这种动力学驱动的过程并揭示中性电荷态双填隙和双空位的形成机制，我们使用密度泛函理论计算生成的小数据集对通用机器学习原子间势进行了微调。在通过辐射和随后的热退火产生缺陷的过程中，会产生与碳相关的缺陷，包括空位和填隙，并且可以迁移形成新的缺陷复合体。 结合关键词看，阅读时应重点关注机器学习原子间势相关的第一性原理设置、对称性分析、能带或响应函数计算，以及这些量与可观测物性的对应关系。

### 5. From Algebraic Completeness to Orbit Separation: Recursive Separating Invariants for Global Neural Network Potential Energy Surfaces

- Source: arXiv
- Date: 2026-10-15T11:20:02Z
- Venue: physics.chem-ph
- Authors: Yiping Hao, Jing Lou, Bina Fu, Dong H. Zhang
- Link: https://arxiv.org/abs/2610.21700v1
- Score: 9.0
- Match: 标题匹配 neural network potential; 近两周发布

**中文摘要：** 置换不变多项式 (PIP) 为全局势能面 (PES) 提供了系统可改进的、保持对称性的表示，但其作为神经网络描述符的高计算成本限制了其在大型分子系统中的应用。基本不变量 (FI) 形成代数完备的生成集，大大减少了描述符的数量，并使神经网络 PES 能够用于更大的系统。然而，随着分子尺寸和复杂性的增加，PES 评估的计算成本仍然很高。 在这里，我们引入了递归分离不变量（RSI），将描述符设计原则从代数完备性转变为轨道分离。 RSI 是通过相关顺序和递归深度系统构建的，提供了计算效率更高的表示。反应性和非反应性系统的基准测试表明，基于 RSI 的神经网络 (RSI-NN) PES 的评估速度比 FI-NN 同类产品快大约一个数量级，并且系统相关的预测精度在多种情况下相当。 这些结果确立了轨道分离作为为全局神经网络 PES 开发有效的对称性保持描述符的有前途的原理。
**讨论重点：** 在这里，我们引入了递归分离不变量（RSI），将描述符设计原则从代数完备性转变为轨道分离。基本不变量 (FI) 形成代数完备的生成集，大大减少了描述符的数量，并使神经网络 PES 能够用于更大的系统。 结合关键词看，阅读时应重点关注神经网络势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 6. Instability-driven segregation of V group transition metals on HEB$_2$ grain boundaries influencing enhanced mechanical properties

- Source: arXiv
- Date: 2026-10-18T14:26:28Z
- Venue: cond-mat.mtrl-sci
- Authors: Daniil Alekseev, Viktor S. Baidyshev, Alexander G. Kvashnin
- Link: https://arxiv.org/abs/2610.25295v1
- Score: 8.0
- Match: 摘要匹配 MACE potential; 近两周发布

**中文摘要：** 五种金属在 (Hf,Ta,Ti,Nb,Zr)B$_2$ (HEB$_2$) 中共享一个公共子晶格。大多数高熵材料都是以烧结陶瓷形式的多晶材料生产的。哪些金属种类位于晶界的问题仍然未知。在这里，我们使用密度泛函理论（DFT）计算了五种二硼化物和HEB$_2$中四种晶界的晶界能$γ_{GB}$。 我们使用 COHP 分析了这些边界处的键合，并使用蒙特卡罗/分子动力学和针对该系统进行微调的 MACE 势，对 HEB$_2$ 的六个边界处的阳离子分离进行了采样（有序和一般）。根据我们的结果$γ_{GB}$按组划分：V族二硼化物NbB$_2$和TaB$_2$在四种GB中的三种中形成了大约IV族能量一半的边界，范围从0.8到2.7，而2.5--4.8~J/m$^2$。 COHP在费米能级上表现出显着差异，即NbB$_2$和TaB$_2$的Me--B键在费米能级($E_F$)处呈反键合，而在GB处成键，而它们的综合强度几乎没有变化。在 HEB$_2$ 中，偏析遵循类似的模式：Nb 和 Ta 在 6 个晶界中的 5 个处富集，包括一般晶界，在 2000~K 时高达 23--35~at.\%，尽管原子的尺寸有利于扩展位点中的 Zr 和 Hf。对于 300~K 张力下的随机边界，偏析的 $Σ193$ 晶界可以承受 26 对 20~GPa 的压力。 HEB$_2$ 的晶界由 V 族金属组成，如二元化合物的边界能及其在费米能级的键合所表明的那样。 (Hf,Ta,Ti,Nb,Zr)B$_2$的晶界优先包括Nb和Ta。这降低了晶界能并强化了晶界。这包括较低的边界能量并改变 NbB$_2$ 和 TaB$_2$ 中的费米能级键合。
**讨论重点：** 五种金属在 (Hf,Ta,Ti,Nb,Zr)B$_2$ (HEB$_2$) 中共享一个公共子晶格。大多数高熵材料都是以烧结陶瓷形式的多晶材料生产的。 结合关键词看，阅读时应重点关注MACE 势函数相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 7. Theoretical Investigation of Oxygen-Vacancy Diffusion in SrTiO$_3$ using Neural Network Potentials

- Source: arXiv
- Date: 2026-10-12T10:10:35Z
- Venue: cond-mat.mtrl-sci
- Authors: Kazutaka Nishiguchi, Ryota Yamamoto, Seiichiro Ten-no
- Link: https://arxiv.org/abs/2610.16521v1
- Score: 8.0
- Match: 标题匹配 neural network potential; 近两周发布

**中文摘要：** 氧空位的形成和扩散在确定 SrTiO$_3$ (STO) 的电子和原子输运特性方面发挥着重要作用。对此类点缺陷的精确分析需要足够大规模和长时间的分子动力学（MD）模拟；然而，基于密度泛函理论（DFT）的从头开始MD（AIMD）对氧空位动力学的直接研究仅限于相对较小的系统和较短的时间尺度，因为其计算成本较高。 在这项研究中，我们使用 AIMD 模拟生成的参考数据集开发了用于原始缺氧 STO 的神经网络潜力 (NNP)。经过训练的 NNP 模型准确地再现了原始 STO 和包含氧空位的 STO 的 DFT 参考能量、原子力和维里尔。 NNP 还再现了总能量和氧空位形成能的超晶胞尺寸依赖性，包括外推到稀极限的形成能。 然后使用 NNP (NNP-MD) 进行大规模和长时间的 MD 模拟，以研究氧空位扩散。与传统经典 MD 模拟获得的氧空位扩散系数相比，所得氧空位扩散系数与实验数据的吻合程度要好得多。阿伦尼乌斯分析得出氧空位迁移焓为 0.64 eV，与实验值 0.67 eV 非常一致。 这些结果表明，基于第一原理数据训练的 NNP 为研究钙钛矿氧化物中的缺陷形成和长期空位传输提供了准确且计算高效的框架。
**讨论重点：** 在这项研究中，我们使用 AIMD 模拟生成的参考数据集开发了用于原始缺氧 STO 的神经网络潜力 (NNP)。经过训练的 NNP 模型准确地再现了原始 STO 和包含氧空位的 STO 的 DFT 参考能量、原子力和维里尔。 结合关键词看，阅读时应重点关注神经网络势相关的模拟体系、时间尺度、温度条件、动力学稳定性，以及有限温度性质对势函数质量的敏感性。

### 8. Long-Range Machine Learning Interatomic Potentials for Defect Energetics in SrTiO$_3$

- Source: arXiv
- Date: 2026-09-30T22:33:45Z
- Venue: cond-mat.mtrl-sci
- Authors: Yee Chit Wong, Marcel F. Langer, Reinhard J. Maurer, Nicholas D. M. Hine
- Link: https://arxiv.org/abs/2610.00794v1
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential

**中文摘要：** 机器学习原子间势（MLIP）近年来发展迅速，但大多数模型本质上仍然是半局域的，并且忽略了长程静电相互作用。为了解决这一限制，出现了越来越多的远程模型，但比较它们在物理现实系统上的性能的系统基准仍然很少。 在这项工作中，我们根据短程基线 MACE 模型评估了三种远程 MLIP——MACE-POLAR、MACE-LES 和 LOREM，评估它们捕获长程库仑相互作用的能力，从理想化的合成点电荷系统发展到现实晶体结构的第一原理数据。这一进展使我们能够将模型学习静电相互作用的能力与 DFT 总能量中存在的许多竞争能量贡献（例如介电屏蔽和交换相关）隔离开来。 作为物理驱动的基准系统，我们重点关注具有 Sr--O 肖特基空位对的钛酸锶 SrTiO$_3$，这种材料中长程电荷相互作用发挥着核心作用，并且是研究带电极化子和其他电子和光学特性的天然垫脚石。 在此基准的基础上，我们进一步检查了 Sr-O 肖特基对存在下的氧空位迁移，使用爬升图像微移弹性带计算和分子动力学来获得激活势垒作为空位对分离的函数，为每个模型捕获控制缺陷传输的静电效应的能力提供进一步的外推测试。
**讨论重点：** 这一进展使我们能够将模型学习静电相互作用的能力与 DFT 总能量中存在的许多竞争能量贡献（例如介电屏蔽和交换相关）隔离开来。作为物理驱动的基准系统，我们重点关注具有 Sr--O 肖特基空位对的钛酸锶 SrTiO$_3$，这种材料中长程电荷相互作用发挥着核心作用，并且是研究带电极化子和其他电子和光学特性的天然垫脚石。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 9. Reticulating Local Dynamics in Three-Dimensional Covalent Organic Frameworks

- Source: arXiv
- Date: 2026-10-17T03:30:37Z
- Venue: cond-mat.mtrl-sci
- Authors: Francesco Tavani, Saber Mirzaei, M. Saeed Mirzaei, Jian Yin, Yen-hsu Lin, Caden Myers
- Link: https://arxiv.org/abs/2610.24418v1
- Score: 7.0
- Match: 摘要匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 在共价有机框架（COF）中，构建单元的几何形状预先决定了框架的结构，但将COF连接体与控制客体吸附和扩散以及机械响应的局部运动相关的可比较的设计原理仍然遥不可及。 在这里，我们将同步加速器 X 射线对分布函数 (PDF) 分析与机器学习原子间势加速的分子动力学 (MD) 模拟相结合，以解析和比较两个三维亚胺连接 COF 的局部动力学，这两个结构单元的几何形状和刚性不同。 两者均由相同的 4 连接的方形平面连接体 $4,4',4'',4'''$-(pyrene-1,3,6,8-tetrayl)tetraaniline (PyTTA) 构成，并与 12 连接的纳米石墨烯六基{[3,5-双($p$-甲酰基苯基)-4,6-二甲氧基苯基]}六苯并晕形成网状COF-412，{[(HBC-LA$_{12}$)(PyTTA)$_3$]}$_{\mathit{imine}}$，并与6-连接的三蝶烯2,3,6,7,14,15-六(4-甲酰基苯基)三蝶烯得到COF-564， {[(Trip-CHO)$_2$(PyTTA)$_3$]}$_{\mathit{亚胺}}$。 PDF-MD方法解析了所有COF连接体运动的幅度、时间尺度和空间范围，将稠合芳族核的有限解放与它们携带的悬垂芳环的较大重新取向倾斜以及网络内整个连接体的平移分开。
**讨论重点：** 在共价有机框架（COF）中，构建单元的几何形状预先决定了框架的结构，但将COF连接体与控制客体吸附和扩散以及机械响应的局部运动相关的可比较的设计原理仍然遥不可及。 在这里，我们将同步加速器 X 射线对分布函数 (PDF) 分析与机器学习原子间势加速的分子动力学 (MD) 模拟相结合，以解析和比较两个三维亚胺连接 COF 的局部动力学，这两个结构单元的几何形状和刚性不同。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 10. Benchmarking machine-learning interatomic potentials using classical force fields

- Source: arXiv
- Date: 2026-10-09T18:56:31Z
- Venue: cond-mat.mtrl-sci
- Authors: Johannes Sandberg, Geneviève Dusson, Julien Lam
- Link: https://arxiv.org/abs/2610.14239v1
- Score: 7.0
- Match: 摘要匹配 neural network potential; 摘要匹配 MACE potential

**中文摘要：** 我们通过测试几种著名的机器学习原子间势（线性原子团簇扩展、Behler-Parrinello 高维神经网络势和基于图神经网络的 MACE 势）对它们拟合经典势（如 Lennard-Jones 和 Stillinger-Weber 势）的性能进行理性比较。 由此，我们评估了它们在几个方面的优点和局限性：不同的训练数据集大小、对噪声的鲁棒性、碳足迹，以及重现径向分布函数作为可观察示例的能力。总体而言，MACE 模型能够最准确地再现势能面，几乎没有过度拟合的迹象，但计算成本很高，这凸显了计算材料科学中模型选择的重要问题。
**讨论重点：** 我们通过测试几种著名的机器学习原子间势（线性原子团簇扩展、Behler-Parrinello 高维神经网络势和基于图神经网络的 MACE 势）对它们拟合经典势（如 Lennard-Jones 和 Stillinger-Weber 势）的性能进行理性比较。 由此，我们评估了它们在几个方面的优点和局限性：不同的训练数据集大小、对噪声的鲁棒性、碳足迹，以及重现径向分布函数作为可观察示例的能力。 结合关键词看，阅读时应重点关注神经网络势、MACE 势函数相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

## 凝聚态物理强关联体系和多铁性质

### 1. Finite-width altermagnetic quantum rings: angular-channel hybridization and Aharonov--Bohm physics

- Source: arXiv
- Date: 2026-10-21T23:43:38Z
- Venue: cond-mat.mes-hall, quant-ph
- Authors: Edilberto O. Silva
- Link: https://arxiv.org/abs/2610.30536v1
- Score: 22.0
- Match: 标题匹配 altermagnetic; 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS $ N_e = 1400 $和$ 1800 $的独立收敛计算建立了有限场窗口中重建的费米边缘和磁响应以及整个AB通量周期内的持续电流。常规参考分析将径向子带去除（ dHvA型循环）与更精细的有限环壳振荡分开；我们不将全局傅里叶谱分配给未经验证的变磁场扫描。 少电子热响应是从精确的固定粒子数规范划分函数获得的，避免了固定平均数近似的有限系统误差。圆形模型支持平衡充电电流，但没有持续的自旋电流。
**讨论重点：** 我们研究一个有限宽度的二维量子环，具有二次$ d $ -波改变磁项， Tan--Inkson约束，垂直磁场和独立可调的Aharonov-Bohm （ AB ）通量。圆形模型支持平衡充电电流，但没有持续的自旋电流。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 2. Emergent altermagnetism in (LaVO$_3$)$_n$/(LaNiO$_3$)$_m$ superlattices from interfacial charge transfer and octahedral tilts

- Source: arXiv
- Date: 2026-10-21T19:31:42Z
- Venue: cond-mat.str-el, cond-mat.mtrl-sci
- Authors: Gustavo H. Cassemiro, Walber H. Brito
- Link: https://arxiv.org/abs/2610.30371v1
- Score: 22.0
- Match: 标题匹配 altermagnetism; 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 使用第一原理计算，我们证明了(LaVO $_3 $) $_n $/(LaNiO $_3 $) $_m $超晶格中出现了改变磁性，其中$ (n, m) = (1,1), (2,2) $和$ (2,4) $ ，来自界面电荷转移和八面体倾斜的相互作用。电荷转移驱动系统朝向V $ ^ {4 +} $和Ni $ ^ {2 +} $配置，将顺磁性镍酸盐层转变为磁性活跃的亚晶格。 由此产生的$ C $型反铁磁序，结合$ a ^ -b ^ + c ^ - $或$ a ^ -b ^ -c ^ - $八面体倾斜，仅通过非对称运算连接相反自旋亚晶格，产生$ d $ -波自旋分裂，无自旋轨道耦合。在DFT + U中，绝缘(LVO) $_1 $/(LNO) $_1 $超晶格中的分裂达到118 meV ，约为批量LaVO $_3 $计算的两倍，并且随着镍酸盐层变得更厚而减小。 我们的研究结果表明，这种分裂由V和Ni亚晶格承载，其近一半的重量通过$ p $ - $ d $共价作用在氧$ 2p $态上。因此，界面电荷转移成为氧化物异质结构中工程改变磁性的\ textit {设计}原理。
**讨论重点：** 因此，界面电荷转移成为氧化物异质结构中工程改变磁性的\ textit {设计}原理。电荷转移驱动系统朝向V $ ^ {4 +} $和Ni $ ^ {2 +} $配置，将顺磁性镍酸盐层转变为磁性活跃的亚晶格。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 3. Extreme competition between stripes and superconductivity in the hole-doped Hubbard model

- Source: arXiv
- Date: 2026-10-21T18:33:57Z
- Venue: cond-mat.str-el, cond-mat.dis-nn, cond-mat.supr-con
- Authors: Ao Chen, Johnnie Gray, Si-Jing Du, Garnet Kin-Lic Chan
- Link: https://arxiv.org/abs/2610.30321v1
- Score: 18.0
- Match: 标题匹配 Hubbard model; 摘要匹配 tensor network; 最近 3 天发布

**中文摘要：** 二维哈伯德模型最初是作为铜酸盐高温超导体中均匀$ d $ -波超导性的最小模型提出的，但最近在现实掺杂条件下的相关参数计算往往会发现其他基态。此外，由于不同计算方法的内在偏差，这些结果仍存在不确定性。 QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS 我们的工作重新平衡了哈伯德模型在相关参数体系中支持单一主导秩序的叙述，以描绘条纹和超导性之间的极端竞争。
**讨论重点：** 二维哈伯德模型最初是作为铜酸盐高温超导体中均匀$ d $ -波超导性的最小模型提出的，但最近在现实掺杂条件下的相关参数计算往往会发现其他基态。此外，由于不同计算方法的内在偏差，这些结果仍存在不确定性。 结合关键词看，阅读时应重点关注Hubbard 模型、张量网络相关的有效模型参数、电子关联强度、相图边界以及可与实验对照的谱学或输运信号。

### 4. $π$-Flux Tuning of Quantum Paramagnetism in the Triangular-Lattice Hubbard Model

- Source: arXiv
- Date: 2026-10-21T18:07:15Z
- Venue: cond-mat.str-el
- Authors: Zhaochen Liu, Andreas Feuerpfeil, Ronny Thomale
- Link: https://arxiv.org/abs/2610.30290v1
- Score: 18.0
- Match: 标题匹配 Hubbard model; 摘要匹配 density matrix renormalization group; 最近 3 天发布

**中文摘要：** 我们比较了两个半填充的时间反转对称三角晶格Hubbard模型：零通量模型和交错$ π $ -通量模型，其中零和$ π $通量通过反向三角形。虽然两者在强耦合极限中以领先顺序简化为相同的海森堡模型，但它们不同的电荷波动分布产生不同的量子顺磁性体系。 将强耦合扩张与无限密度矩阵重整群（ iDMRG ）计算相结合，我们发现零通量模型的正环交换促进了自发手性，这与其在中间耦合处的手性自旋液体的概念一致。在交错- $ π $ -通量模型中，其非相互作用极限是狄拉克半金属，环交换改变符号，不利于手性顺序，我们发现没有可解的标量手性。 这使得通量调谐环交换在有限耦合下成为手性和非手性量子顺磁体之间的有效鉴别器。
**讨论重点：** 我们比较了两个半填充的时间反转对称三角晶格Hubbard模型：零通量模型和交错$ π $ -通量模型，其中零和$ π $通量通过反向三角形。虽然两者在强耦合极限中以领先顺序简化为相同的海森堡模型，但它们不同的电荷波动分布产生不同的量子顺磁性体系。 结合关键词看，阅读时应重点关注Hubbard 模型、密度矩阵重整化群相关的有效模型参数、电子关联强度、相图边界以及可与实验对照的谱学或输运信号。

### 5. Microscopic origin of field-induced multiferroicity in Ni3TeO6

- Source: arXiv
- Date: 2026-10-21T08:45:40Z
- Venue: cond-mat.mtrl-sci
- Authors: J. Lass, R. Toft-Petersen, A. A. Turrini, Ø. S. Fjellvåg, B. Decrausaz, K. M. L. Krighaar
- Link: https://arxiv.org/abs/2610.29420v1
- Score: 18.0
- Match: 标题匹配 multiferroic; 摘要匹配 multiferroic materials; 最近 3 天发布

**中文摘要：** QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS 在这里，我们使用中子散射技术的组合来揭示这种多铁跃迁的微观起源。我们确定了有限的Dzyaloshinskii-Moriya交换项的存在，从而产生在磁场中软化的非互易的手性自旋波。它们的凝聚改变了控制电极化并驱动离子位移的磁性结构，从而耦合了磁、电和晶格的自由度。 我们的研究表明，中子散射是阐明多铁性材料中微观相互作用的强大技术，为下一代电子设备的设计提供了信息。
**讨论重点：** 我们的研究表明，中子散射是阐明多铁性材料中微观相互作用的强大技术，为下一代电子设备的设计提供了信息。特别有趣的例子是具有有序参数之间交叉耦合的多铁性材料。 结合关键词看，阅读时应重点关注多铁性、多铁材料相关的极化翻转、磁电耦合、自旋-晶格耦合以及多铁序参量之间的相互制约。

### 6. Piezo-Kerr effect in altermagnets and noncollinear antiferromagnets

- Source: arXiv
- Date: 2026-10-22T08:49:03Z
- Venue: cond-mat.mtrl-sci, cond-mat.mes-hall
- Authors: Yuqi Liu, Qiu-Shi Huang, Xinfeng Chen, Yilin Han, Run-Wu Zhang, Zhi-Ming Yu
- Link: https://arxiv.org/abs/2610.30929v1
- Score: 16.0
- Match: 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS
**讨论重点：** 对称性通常被视为对物理响应的约束，但它也可以用于设计控制它们的场。这里，我们采用表示匹配原则来识别阶参数的共轭域，并将其应用于响应张量。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 7. Sign-problem-free Bosonic Auxiliary Field Quantum Monte Carlo

- Source: arXiv
- Date: 2026-10-22T16:48:36Z
- Venue: cond-mat.str-el, cond-mat.quant-gas, cond-mat.stat-mech
- Authors: Yin-Kai Yu, Zhong-Chao Wei, Zi-Xiang Li
- Link: https://arxiv.org/abs/2610.31541v1
- Score: 15.0
- Match: 摘要匹配 Hubbard model; 摘要匹配 quantum many-body; 最近 3 天发布

**中文摘要：** QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS
**讨论重点：** 在这里，我们开发了一种玻色子辅助场量子蒙特卡罗（ BAFQMC ）方法，并严格证明时间反转对称性和反射正性都为无符号问题模拟提供了一般的充分条件。几何挫折感使得这种屏障对于相互作用的玻色子尤其尖锐。 结合关键词看，阅读时应重点关注Hubbard 模型、量子多体相关的有效模型参数、电子关联强度、相图边界以及可与实验对照的谱学或输运信号。

### 8. Ferroelastic Reversal Magnon Thermal Hall Effect in a Fully Compensated Ferrimagnet

- Source: arXiv
- Date: 2026-10-22T05:01:12Z
- Venue: cond-mat.mes-hall
- Authors: Yingxi Bai, Zihan Chen, Chengwang Niu, Ming Yang
- Link: https://arxiv.org/abs/2610.30733v1
- Score: 15.0
- Match: 摘要匹配 altermagnetic; 摘要匹配 altermagnet; 最近 3 天发布

**中文摘要：** QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS 因此，与[C2 || C4z]相关的两个正交完全补偿的铁磁变体表现出具有相反符号的磁热霍尔响应，而该响应在中间改变磁相中消失。第一原理计算进一步确定单层V2SSe是实现横向磁子传输的拟议铁弹性控制的有希望的候选材料。 值得注意的是，铁弹性开关驱动双磁电子波段重建，实现了磁子热霍尔效应的非易失性逆转，同时产生各向异性轨道霍尔响应和不同的磁光谱，作为互补的传输和光学指纹。我们的研究结果将铁弹性确定为零净磁化系统中非挥发性磁子控制和多通道状态识别的有效途径。
**讨论重点：** 最小Heisenberg-Dzyaloshinskii-Moriya模型表明，铁弹性开关可以重新定向晶格各向异性，从而重建手性分辨的磁子带和Berry曲率分布。在这里，我们将铁弹性开关确立为操纵完全补偿铁磁体中的强子横向响应的有效途径。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 9. Unrestricted Binary Tree State for the Fermionic Hubbard Model

- Source: arXiv
- Date: 2026-10-21T20:04:02Z
- Venue: cond-mat.str-el
- Authors: Mahroo Mirabdolhagh Hazaveh, Armin Khamoshi, Fei Gao, Thomas M. Henderson, Gustavo E. Scuseria
- Link: https://arxiv.org/abs/2610.30399v1
- Score: 15.0
- Match: 标题匹配 Hubbard model; 最近 3 天发布

**中文摘要：** QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS 这为成对的ansatz提供了一种机制，以描述在大U/t下主导排斥哈伯德模型的单个占用配置。我们发现，与pCCD相比，不受限制的BTS在排斥状态下密切接近优化的DOCI ，显著改善了AGP ，并更准确地再现了DOCI密度相关性
**讨论重点：** 在这里，我们使用受限和不受限的轨道将二叉树状态扩展到费米子半填充哈伯德模型。虽然ansatz在其优化配对基础上的资历为零，但其在原始Hubbard站点基础上的扩展可以包含非零站点资历字符，而无限制的轨道优化通过独立的旋转升降轨道提供了额外的灵活性。 结合关键词看，阅读时应重点关注Hubbard 模型相关的有效模型参数、电子关联强度、相图边界以及可与实验对照的谱学或输运信号。

### 10. Projective symmetry groups beyond spin-$1/2$: Classifying integer-spin quantum spin liquids

- Source: arXiv
- Date: 2026-10-21T17:08:50Z
- Venue: cond-mat.str-el
- Authors: Atanu Maity, Chunxiao Liu, Rhine Samajdar, Yasir Iqbal
- Link: https://arxiv.org/abs/2610.30048v1
- Score: 15.0
- Match: 标题匹配 quantum spin liquid; 最近 3 天发布

**中文摘要：** QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS 每个站点上具有相同约束的时间反转对称$\ mathrm {U} (1) $状态只能在每个单元格的站点数为$ 2S +1 $的倍数时间隙。我们将形式主义应用于自旋- $ 1 $钻石晶格，在沮丧的A位尖晶石中实现，并找到十个完全对称的Ansätze到第二个邻居。在平均场水平的$ J_1 $ - $ J_2 $海森堡模型中，基态取决于约束的实施方式。 对于粒子和空穴表示，最低状态是完全间隙的$\ mathrm {U} (1) $状态，其两个子格位于相反的约束扇区中，其中一个是等效于成对Ansatz的仪表。该分类为其他晶格和其他材料上的整数自旋量子自旋液体提供了起点。
**讨论重点：** 四分之一个世纪前引入的温氏射影对称群（ PSG ）将对称量子自旋液体的分类简化为代数问题，并从此指导了自旋- $ 1/2 $模型和材料的研究。在平均场水平的$ J_1 $ - $ J_2 $海森堡模型中，基态取决于约束的实施方式。 结合关键词看，阅读时应重点关注量子自旋液体相关的新方法的假设、训练或计算流程、适用体系，以及与已有方法相比的优势和局限。
