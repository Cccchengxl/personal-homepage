# Latest papers for 程旭丽

Updated: 2026-11-05T04:49:05.629360+00:00
Window: last 14 days

## Notes

- arXiv query failed for 机器学习分子动力学模拟与热力学性质: HTTP Error 429: Unknown Error
- 机器学习分子动力学模拟与热力学性质 kept previous papers because the current query returned 0 results.
- arXiv query failed for 凝聚态物理强关联体系和多铁性质: HTTP Error 429: Unknown Error
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

**中文摘要：** 五种金属在 (Hf,Ta,Ti,Nb,Zr)B$_2$ (HEB$_2$) 中共享一个公共子晶格。大多数高熵材料都是以烧结陶瓷形式的多晶材料生产的。哪些金属种类位于晶界的问题仍然未知。在这里，我们使用密度泛函理论（DFT）计算了五种二硼化物和HEB$_2$中四种晶界的晶界能$γ_{GB}$。 我们使用 COHP 分析了这些边界处的键合，并使用蒙特卡罗/分子动力学和针对该系统进行微调的 MACE 势，对 HEB$_2$ 的六个边界处的阳离子分离进行了采样（有序和一般）。根据我们的结果$γ_{GB}$按组划分：V族二硼化物NbB$_2$和TaB$_2$在四种GB中的三种中形成了大约IV族能量一半的边界，范围从0.8到2.7，而2.5--4.8~J/m$^2$。 COHP在费米能级上表现出显着差异，即NbB$_2$和TaB$_2$的Me--B键在费米能级($E_F$)处呈反键合，而在GB处成键，而它们的综合强度几乎没有变化。在 HEB$_2$ 中，偏析遵循类似的模式：Nb 和 Ta 在 6 个晶界中的 5 个处富集，包括一般晶界，在 2000~K 时高达 23--35~at.\%，尽管原子的尺寸有利于扩展位点中的 Zr 和 Hf。对于 300~K 张力下的随机边界，偏析的 $Σ193$ 晶界可以承受 26 对 20~GPa 的压力。 HEB$_2$ 的晶界由 V 族金属组成，如二元化合物的边界能及其在费米能级的键合所示。 (Hf,Ta,Ti,Nb,Zr)B$_2$的晶界优先包括Nb和Ta。这降低了晶界能并强化了晶界。这包括较低的边界能量并改变 NbB$_2$ 和 TaB$_2$ 中的费米能级键合。
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

**中文摘要：** 机器学习原子间势（MLIP）近年来发展迅速，但大多数模型本质上仍然是半局域的，并且忽略了长程静电相互作用。为了解决这一限制，出现了越来越多的远程模型，但比较它们在物理现实系统上的性能的系统基准仍然很少。 在这项工作中，我们根据短程基线 MACE 模型评估了三种远程 MLIP——MACE-POLAR、MACE-LES 和 LOREM，评估它们捕获长程库仑相互作用的能力，从理想化的合成点电荷系统发展到现实晶体结构的第一原理数据。这一进展使我们能够将模型学习静电相互作用的能力与 DFT 总能量中存在的许多竞争能量贡献（例如介电屏蔽和交换相关）隔离开来。 作为物理驱动的基准系统，我们重点关注具有 Sr--O 肖特基空位对的钛酸锶 SrTiO$_3$，这种材料中长程电荷相互作用发挥着核心作用，并且是研究带电极化子和其他电子和光学特性的天然垫脚石。 在此基准的基础上，我们进一步检查了 Sr--O 肖特基对存在下的氧空位迁移，使用爬升图像微移弹性带计算和分子动力学来获得激活势垒作为空位对分离的函数，从而对每个模型捕获控制缺陷传输的静电效应的能力进行进一步的外推测试。
**讨论重点：** 这一进展使我们能够将模型学习静电相互作用的能力与 DFT 总能量中存在的许多竞争能量贡献（例如介电屏蔽和交换相关）隔离开来。作为物理驱动的基准系统，我们重点关注具有 Sr--O 肖特基空位对的钛酸锶 SrTiO$_3$，这种材料中长程电荷相互作用发挥着核心作用，并且是研究带电极化子和其他电子和光学特性的天然垫脚石。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 9. Reticulating Local Dynamics in Three-Dimensional Covalent Organic Frameworks

- Source: arXiv
- Date: 2026-10-17T03:30:37Z
- Venue: cond-mat.mtrl-sci
- Authors: Francesco Tavani, Saber Mirzaei, M. Saeed Mirzaei, Jian Yin, Yen-hsu Lin, Caden Myers
- Link: https://arxiv.org/abs/2610.24418v1
- Score: 7.0
- Match: 摘要匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 在共价有机框架（COF）中，构建单元的几何形状预先决定了框架的结构，但将COF连接体与控制客体吸附和扩散以及机械响应的局部运动相关的可比较的设计原理仍然遥不可及。 在这里，我们将同步加速器 X 射线对分布函数 (PDF) 分析与机器学习原子间势加速的分子动力学 (MD) 模拟相结合，以解析和比较两个三维亚胺连接 COF 的局部动力学，这两个结构单元的几何形状和刚性不同。 两者均由相同的 4 连接的方形平面连接体 $4,4',4'',4'''$-(pyrene-1,3,6,8-tetrayl)tetraaniline (PyTTA) 构成，并与 12 连接的纳米石墨烯六基{[3,5-双($p$-甲酰基苯基)-4,6-二甲氧基苯基]}六苯并苯并成网状COF-412，{[(HBC-LA$_{12}$)(PyTTA)$_3$]}$_{\mathit{imine}}$，并与6-连接的三蝶烯2,3,6,7,14,15-六(4-甲酰基苯基)三蝶烯得到COF-564， {[(Trip-CHO)$_2$(PyTTA)$_3$]}$_{\mathit{亚胺}}$。 PDF-MD方法解析了所有COF连接体运动的幅度、时间尺度和空间范围，将稠合芳族核的有限解放与它们携带的悬垂芳环的较大重新取向倾斜以及网络内整个连接体的平移分开。
**讨论重点：** 在共价有机框架（COF）中，构建单元的几何形状预先决定了框架的结构，但将COF连接体与控制客体吸附和扩散以及机械响应的局部运动相关的可比较的设计原理仍然遥不可及。 在这里，我们将同步加速器 X 射线对分布函数 (PDF) 分析与机器学习原子间势加速的分子动力学 (MD) 模拟相结合，以解析和比较两个三维亚胺连接 COF 的局部动力学，这两个结构单元的几何形状和刚性不同。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 10. Benchmarking machine-learning interatomic potentials using classical force fields

- Source: arXiv
- Date: 2026-10-09T18:56:31Z
- Venue: cond-mat.mtrl-sci
- Authors: Johannes Sandberg, Geneviève Dusson, Julien Lam
- Link: https://arxiv.org/abs/2610.14239v1
- Score: 7.0
- Match: 摘要匹配 neural network potential; 摘要匹配 MACE potential

**中文摘要：** 我们通过测试几种著名的机器学习原子间势（线性原子团簇扩展、Behler-Parrinello 高维神经网络势和基于图神经网络的 MACE 势）对它们拟合经典势（例如 Lennard-Jones 和 Stillinger-Weber 势）的性能进行理性比较。 由此，我们评估了它们在几个方面的优点和局限性：不同的训练数据集大小、对噪声的鲁棒性、碳足迹，以及重现径向分布函数作为可观察示例的能力。总体而言，MACE 模型能够最准确地再现势能面，几乎没有过度拟合的迹象，但计算成本很高，这凸显了计算材料科学中模型选择的重要问题。
**讨论重点：** 我们通过测试几种著名的机器学习原子间势（线性原子团簇扩展、Behler-Parrinello 高维神经网络势和基于图神经网络的 MACE 势）对它们拟合经典势（例如 Lennard-Jones 和 Stillinger-Weber 势）的性能进行理性比较。 由此，我们评估了它们在几个方面的优点和局限性：不同的训练数据集大小、对噪声的鲁棒性、碳足迹，以及重现径向分布函数作为可观察示例的能力。 结合关键词看，阅读时应重点关注神经网络势、MACE 势函数相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

## 凝聚态物理强关联体系和多铁性质

### 1. Two-Dimensional Magnetic Materials from Ferromagnetism to Altermagnetism: Fabrication, Symmetry, Evidence, and Device Readiness

- Source: arXiv
- Date: 2026-10-28T09:04:30Z
- Venue: cond-mat.mtrl-sci, cond-mat.mes-hall, physics.app-ph
- Authors: Guojian Zhao, Ziang Meng, Li Liu, Zhiyuan Duan, Jingyu Li, Sixu Jiang
- Link: https://arxiv.org/abs/2610.38491v1
- Score: 32.0
- Match: 标题匹配 ferromagnetism; 标题匹配 altermagnetism; 摘要匹配 altermagnetic; 标题匹配 altermagnet

**中文摘要：** 原子薄磁体受成分、厚度、堆叠、应变、缺陷、基底、铁序和界面的控制。本综述使用净磁化强度和动量空间自旋分裂或自旋极化模式作为主要坐标来组织二维 (2D) 磁性，并辅以亚晶格结构和相反自旋亚晶格之间的对称关系。铁磁体通常带有净磁矩；亚铁磁体可以得到完全补偿。 传统的反铁磁体可以保留自旋简并能带，而交替磁体则允许在特定维度的对称约束下发生非相对论性交替自旋分裂。这里介绍的 M1-M4 报告类区分了层解析的原子薄形式、非层解析的薄片或薄膜、批量基准以及理论候选或设计路线；证据类别和排序温度来源是独立报告的。 目前对交变磁相的实验支持主要来自 M2 薄膜和 M3 体基准，将完全验证的原子薄 M1 交变磁相作为开放的实验目标。因此，大多数提出的单层和少层系统都属于 M4 范围，并且有争议的案例阐明了相位分配所需的测量。使用工作温度、读出、切换、域控制、稳定性、可扩展性、接口敏感性和集成难度来定性比较设备准备情况。 可靠的相位分配和设备评估需要在匹配条件下对相同材料形式进行补充测量，最好是在同一样本上或在原位。
**讨论重点：** 这里介绍的 M1-M4 报告类区分了层解析的原子薄形式、非层解析的薄片或薄膜、批量基准以及理论候选或设计路线；证据类别和排序温度来源是独立报告的。本综述使用净磁化强度和动量空间自旋分裂或自旋极化模式作为主要坐标来组织二维 (2D) 磁性，并辅以亚晶格结构和相反自旋亚晶格之间的对称关系。 结合关键词看，阅读时应重点关注铁磁性、交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 2. Light-induced chiral altermagnets from conventional antiferromagnets

- Source: arXiv
- Date: 2026-10-29T16:40:19Z
- Venue: cond-mat.mtrl-sci
- Authors: Jorge Cardenas-Gamboa, Devika Jayadeep, Aritz Leonardo, Gregory A. Fiete, Jeroen van den Brink, Maia G. Vergniory
- Link: https://arxiv.org/abs/2610.40410v1
- Score: 22.0
- Match: 摘要匹配 altermagnetism; 摘要匹配 altermagnetic; 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 交变磁体将补偿共线磁序与动量相关的非相对论自旋分裂相结合，为自旋电子应用提供了新的机会。在这里，我们提出了一种通过相干晶格控制来光学诱导交变磁性的途径。通过对称分析，我们确定了声子畸变，该畸变可以提升传统反铁磁体的自旋简并性，同时保持连接相反自旋子晶格的旋转对称性。 其中，几何手性声子提供了一条特别有吸引力的途径，将交变磁性的出现与结构手性联系起来。以 Fe$_2$TeO$_6$ 作为原型，我们证明了线性偏振中红外脉冲可以通过红外活性声子和光学静音、对称破缺模式之间的负双二次耦合来驱动结构不稳定性。 基于第一原理的晶格动力学揭示了瞬态手性畸变的出现，而电子结构计算表明光诱导结构表现出交变磁性的非相对论自旋分裂特征。我们的结果建立了一条对称引导的途径，通过非线性声子学实现交变磁态的超快光学控制。
**讨论重点：** 在这里，我们提出了一种通过相干晶格控制来光学诱导交变磁性的途径。通过对称分析，我们确定了声子畸变，该畸变可以提升传统反铁磁体的自旋简并性，同时保持连接相反自旋子晶格的旋转对称性。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 3. Topological Quantum Spin Liquids in a Ladder with Majorana fermions and p-wave Superconductivity

- Source: arXiv
- Date: 2026-10-29T15:43:52Z
- Venue: cond-mat.str-el, cond-mat.mes-hall, cond-mat.mtrl-sci
- Authors: Magali Korolev, Fan Yang, Erik S. Sørensen, Karyn Le Hur
- Link: https://arxiv.org/abs/2610.40297v1
- Score: 19.0
- Match: 标题匹配 quantum spin liquid; 摘要匹配 density matrix renormalization group; 最近 3 天发布

**中文摘要：** 在本文中，我们通过一个精确可解的模型来解决梯形系统中整个相图中仅具有短程（自旋）相关性的拓扑量子自旋液体的可能性，该模型表示二维 Kitaev 蜂窝自旋模型到带状几何的推广。该系统通过马约拉纳费米子在基态中以静态方式产生 $\mathbb{Z}_2$ 规范场，然后产生 $0$ 或 $π$ 通量。 通过量子场论的视角、数学和密度矩阵重整化群的结果，我们通过在整个相图上的可观测值导航来展示我们在该模型的几何、拓扑和物理分类方面的进展，该相图呈现出具有自旋间隙的三个自旋液相和马约拉纳费米子意义上的金属相。 我们提出了一种整体边缘对应关系，揭示了在有间隙的相的边缘处存在受保护的零能量马约拉纳费米子，并且还揭示了在拓扑液相的主体中存在流动的马约拉纳费米子。所提出的方法使我们能够区分产生特殊线的砖墙梯子的特性和允许无间隙马约拉纳液相的方梯子的特性。该模型为寻找拓扑量子自旋模型的解决方案带来了一些希望，例如具有 $π$ 通量，在方晶格几何上。 这种方法还允许与拓扑超导模型相对应。
**讨论重点：** 通过量子场论的视角、数学和密度矩阵重整化群的结果，我们通过在整个相图上的可观测值导航来展示我们在该模型的几何、拓扑和物理分类方面的进展，该相图呈现出具有自旋间隙的三个自旋液相和马约拉纳费米子意义上的金属相。 在本文中，我们通过一个精确可解的模型来解决梯形系统中整个相图中仅具有短程（自旋）相关性的拓扑量子自旋液体的可能性，该模型表示二维 Kitaev 蜂窝自旋模型到带状几何的推广。 结合关键词看，阅读时应重点关注量子自旋液体、密度矩阵重整化群相关的自由能路径、相稳定性、热力学量的不确定性，以及势函数误差如何传递到宏观性质。

### 4. Pulse Laser Deposited GaFeO3 Thin Film Grown on FTO: Correlated Ferroic Orders and Strong Magnetodielectric Coupling at Room Temperature

- Source: arXiv
- Date: 2026-10-29T09:33:58Z
- Venue: cond-mat.mtrl-sci, cond-mat.mes-hall
- Authors: Ishita Jana, Sourav Sarkar, Soham Saha, Kalyan Mandal
- Link: https://arxiv.org/abs/2610.39696v1
- Score: 18.0
- Match: 摘要匹配 multiferroic; 摘要匹配 magnetoelectric coupling; 摘要匹配 ferroelectricity; 最近 3 天发布

**中文摘要：** 表现出耦合铁电和磁序的室温单相多铁性材料是下一代磁电存储器和自旋电子技术的有希望的候选者。在这里，我们报道了通过脉冲激光沉积在氟掺杂氧化锡涂层玻璃（FTO）基板上生长约 100.6 nm 厚的多晶正交 GaFeO3 薄膜。核心级 X 射线光电子能谱显示 Fe2+ 浓度降低并抑制氧空位形成，有助于减少漏电流并改善铁电特性。 这些薄膜在室温下表现出强大的亚铁磁性和铁电性，证实了单相中铁序的共存。压电响应力显微镜进一步证明了可逆的局部偏振切换，并伴有矫顽电压为-0.31 V和+1.07 V的不对称蝶形环路。这些薄膜还表现出约1700的高相对介电常数，以及在1 MHz时约2.83的相对较低的介电损耗角正切。 此外，在仅 0.1 kOe 的相对较小的磁场下观察到约 2.3% 的显着磁介电系数，突出了强磁电耦合。这些结果使 GaFeO3 薄膜成为室温多功能器件（主要是低场磁电存储器和自旋电子结构）的有前途的平台。
**讨论重点：** 表现出耦合铁电和磁序的室温单相多铁性材料是下一代磁电存储器和自旋电子技术的有希望的候选者。在这里，我们报道了通过脉冲激光沉积在氟掺杂氧化锡涂层玻璃（FTO）基板上生长约 100.6 nm 厚的多晶正交 GaFeO3 薄膜。 结合关键词看，阅读时应重点关注多铁性、磁电耦合、铁电性相关的极化翻转、磁电耦合、自旋-晶格耦合以及多铁序参量之间的相互制约。

### 5. Nodal magnon spin current at an antiferromagnet/altermagnet junction

- Source: arXiv
- Date: 2026-10-29T02:29:57Z
- Venue: cond-mat.mes-hall, cond-mat.mtrl-sci
- Authors: Koki Mizuno
- Link: https://arxiv.org/abs/2610.39206v1
- Score: 18.0
- Match: 摘要匹配 altermagnetic; 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 我们研究了 d$ 波交变磁体 (AM) 和铁磁体 (FM) 或反铁磁体 (AFM) 之间结点处的热驱动磁振子自旋电流。电流由与界面角度无关的分量和具有 $d$ 波形的角度相关分量组成。 对于亚晶格对称界面，两个结在交变磁畴反转时表现相反：在 FM/AM 结中，角度相关分量是奇数，并且在域上求平均时抵消，而在 AFM/AM 结中，角度无关分量因对称性而消失，角度相关分量在 AFM 的固定 Néel 向量处保留域平均值。 两者都源于选择性隧道效应：当自旋平行时，跨界面键合的一对自旋会传输磁振子，而当自旋平行时则不会，这使得 AFM/AM 结成为磁振子阀：键合自旋反平行的配置会阻止电流到达磁振子的亚晶格混合。 各向异性隧道效应可检测为垂直于 $[310]$ 和 $[130]$ 的界面之间电流的符号反转，并且阀门通过固定界面处的电流大小读取交变磁体相对于反铁磁体的尼尔矢量。
**讨论重点：** 我们研究了 d$ 波交变磁体 (AM) 和铁磁体 (FM) 或反铁磁体 (AFM) 之间结点处的热驱动磁振子自旋电流。电流由与界面角度无关的分量和具有 $d$ 波形的角度相关分量组成。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 6. Electronic liquid crystals and superconductivity from doping a moiré Mott insulator

- Source: arXiv
- Date: 2026-10-29T13:07:04Z
- Venue: cond-mat.str-el, cond-mat.supr-con
- Authors: Yichi Zhang, Yiyu Xia, Zhongdong Han, Jekwan Lee, Brandon Bauer, Kenji Watanabe
- Link: https://arxiv.org/abs/2610.39978v1
- Score: 16.0
- Match: 标题匹配 Mott insulator; 最近 3 天发布

**中文摘要：** 电子液晶，例如条带相和向列相，是具有自发破缺旋转对称性的自组织物质态。它们预计会作为短程和长程库仑相互作用之间的折衷出现在掺杂莫特绝缘体中，并且被认为与高温超导性的出现密切相关，无论是作为竞争级还是交织级。莫尔半导体提供了一个可控平台来探索莫特绝缘体附近的条纹相位和超导性之间的关系。 在这里，我们报告了掺杂莫尔莫特绝缘体中条纹相的一般外观，以及扭曲双层 WSe2 中条纹到超导体量子相变的观察。通过电输运研究揭示了条带相是从高温各向同性相到低温各向异性相的热力学相变，并伴随着费米表面重建。在带材到超导体的转变附近，我们还观察到从金属带材到钉扎绝缘带材的额外热力学相变。 条纹到超导体的转变进一步表现出有趣的自相似性，凸显了两个秩序之间的密切关系。我们的结果为研究莫尔材料中交织的秩序铺平了道路。
**讨论重点：** 莫尔半导体提供了一个可控平台来探索莫特绝缘体附近的条纹相位和超导性之间的关系。它们预计会作为短程和长程库仑相互作用之间的折衷出现在掺杂莫特绝缘体中，并且被认为与高温超导性的出现密切相关，无论是作为竞争级还是交织级。 结合关键词看，阅读时应重点关注Mott 绝缘体相关的有效模型参数、电子关联强度、相图边界以及可与实验对照的谱学或输运信号。

### 7. Spin-Orbit Coupling Response Theory within the Oriented Spin Space Group Framework

- Source: arXiv
- Date: 2026-10-29T14:34:20Z
- Venue: cond-mat.mtrl-sci
- Authors: Yuntian Liu, Xiaobing Chen, Yutong Yu, Jesús Etxebarria, J. Manuel Perez-Mato, Qihang Liu
- Link: https://arxiv.org/abs/2610.40149v1
- Score: 15.0
- Match: 摘要匹配 multiferroic; 摘要匹配 magnetoelectric coupling; 最近 3 天发布

**中文摘要：** 自旋轨道耦合（SOC）在凝聚态物理的广泛现象中发挥着关键作用。最近发展的自旋空间群理论为表征 SOC 相关现象的基本对称破缺特征提供了新的视角，但其全部潜力仍有待探索。在这里，我们提供了一个通用框架，将 SOC 引起的对称性破缺与物理属性的修改和新物理效应的出现联系起来。 该方法结合了最近开发的定向自旋空间群（OSSG）形式主义，它可以明确地描述由 SOC 引起的对称性降低。通过使用连接实数空间和自旋空间的 SOC 张量对 SOC 哈密顿量进行参数化，可以为描述任何物理量的响应张量构造 SOC 分量的扩展。该框架不仅决定了 SOC 引起的响应是否允许对称，还决定了它出现的 SOC 最低阶及其对磁各向异性的依赖性。 作为代表性应用，我们分析了 II 型多铁性材料中的磁电耦合，结果表明不同系统中的磁感应电极化可能是不同阶 SOC 效应的结果，并且可以表现出不同的磁各向异性特征。我们进一步将该理论应用于反铁磁体中的反常霍尔效应和自旋磁化，证明它们在 OSSG 下的独特变换特性允许大的反常霍尔响应与弱自旋磁化共存。 对 MAGNDATA 数据库中材料的高通量分析确定了几种有利于这种共存的基于对称性的材料类别。总体而言，所提出的框架提供了 SOC 引起的现象的统一对称性描述，并为识别 SOC 驱动的功能材料提供了系统的方法。
**讨论重点：** 作为代表性应用，我们分析了 II 型多铁性材料中的磁电耦合，结果表明不同系统中的磁感应电极化可能是不同阶 SOC 效应的结果，并且可以表现出不同的磁各向异性特征。在这里，我们提供了一个通用框架，将 SOC 引起的对称性破缺与物理属性的修改和新物理效应的出现联系起来。 结合关键词看，阅读时应重点关注多铁性、磁电耦合相关的极化翻转、磁电耦合、自旋-晶格耦合以及多铁序参量之间的相互制约。

### 8. Collective sliding relaxor ferroelectricity across thousand-layer van der Waals superstructures

- Source: arXiv
- Date: 2026-10-28T21:17:54Z
- Venue: cond-mat.mtrl-sci, cond-mat.mes-hall, physics.app-ph
- Authors: Nianze Shang, Cuiju Yu, Yucai Lin, Juan C. Arias-Muñoz, Jiajie Qi, Quanlin Guo
- Link: https://arxiv.org/abs/2610.38928v1
- Score: 15.0
- Match: 标题匹配 ferroelectricity; 最近 3 天发布

**中文摘要：** 驰豫铁电体因其异常大的电致伸缩响应而成为最重要的机电材料之一。然而，传统的弛豫行为通常与化学复杂性和结构无序相关，其中局部成分波动产生极性纳米区域，使得这种行为的微观起源难以控制和工程设计。 在这里，我们报告了滑动弛豫铁电（S-RFE），这是一种以前未知的弛豫状态，其中工程堆叠相异质性使得层间协同滑动能够产生集体弛豫行为。通过菱面体氮化硼的堆叠相工程，我们创建了滑动域，其充当极性纳米区域的结构类似物，并通过层间滑动在电场下协同排列。 这种集体状态在大约 300 nm 厚的晶体（相当于大约 1000 个原子层）中产生高达大约 $-1.6\%$ 的可逆机电变形，且滞后可忽略不计。由此产生的电致伸缩系数（$Q_{33}$ 约为 $1200\,\mathrm{m}^{4}\mathrm{C}^{-2}$）超过大多数晶体电致伸缩器的数量级。 与传统的弛豫器不同，传统的弛豫器的机电响应通常会在低温下被偶极冻结所抑制，而 S-RFE 在低至 1.6 K 的温度下仍保持活性，并保持巨大的机电功能。我们的研究结果将滑动弛豫铁电性确立为弛豫行为的新途径，并揭示了如何将原子尺度的层间运动放大为跨越约一千层的集体介观尺度功能，从而为基于范德华材料的机电、光子和量子技术提供了材料设计平台。
**讨论重点：** 我们的研究结果将滑动弛豫铁电性确立为弛豫行为的新途径，并揭示了如何将原子尺度的层间运动放大为跨越约一千层的集体介观尺度功能，从而为基于范德华材料的机电、光子和量子技术提供了材料设计平台。 然而，传统的弛豫行为通常与化学复杂性和结构无序相关，其中局部成分波动产生极性纳米区域，使得这种行为的微观起源难以控制和工程设计。 结合关键词看，阅读时应重点关注铁电性相关的极化翻转、磁电耦合、自旋-晶格耦合以及多铁序参量之间的相互制约。

### 9. The Flexoelectric Twist: Persistence of Heavy Fermion Picture in Small-Angle Twisted Bilayer Graphene

- Source: arXiv
- Date: 2026-10-28T05:44:01Z
- Venue: cond-mat.mes-hall
- Authors: Qirong Yao, Ka Cheuk Fan, Tianyu Qiao, Hao Shi, Xi Dai, Berthold Jäck
- Link: https://arxiv.org/abs/2610.38305v1
- Score: 15.0
- Match: 标题匹配 heavy fermion; 最近 3 天发布

**中文摘要：** 第一个魔角 ($θ\approx1.05^{\circ}$) 附近的扭曲双层石墨烯 (TBG) 具有平坦的带，为探索强相关和拓扑相提供了肥沃的土壤。在较小的扭转角（$θ<1^{\circ}$）下，晶格松弛会深刻地改变莫尔条纹景观。不同长度尺度的莫尔晶格重建通过机电耦合影响电子结构的程度仍未解决。 QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS 原子晶格膨胀的额外包含产生了强烈的挠曲电响应，显着打破了粒子空穴对称性，将 AA 位点处的紧凑、局域 $f$ 态推低了能量。因此，这些重费米子态与 AB/BA 位点的流动 $c$ 电子能量共存。我们的空间分辨光谱测量定量地可视化了这种共存，证实了重费米子模型在小角度状态 $θ<1^{\circ}$ 中的持久性。 我们的研究结果为柔印电如何影响小角度 TBG 的低能电子结构提供了微观见解。更广泛地说，我们的研究将小角度 TBG 确立为一类新型莫尔材料，以探索相互作用的近藤晶格问题，分别通过扭转角和静电背栅实现 $f-$ 占据和 $c-$ 密度的高可调性。
**讨论重点：** 更广泛地说，我们的研究将小角度 TBG 确立为一类新型莫尔材料，以探索相互作用的近藤晶格问题，分别通过扭转角和静电背栅实现 $f-$ 占据和 $c-$ 密度的高可调性。我们的空间分辨光谱测量定量地可视化了这种共存，证实了重费米子模型在小角度状态 $θ<1^{\circ}$ 中的持久性。 结合关键词看，阅读时应重点关注重费米子相关的有效模型参数、电子关联强度、相图边界以及可与实验对照的谱学或输运信号。

### 10. Quasi-Phases of Quantum Matter

- Source: arXiv
- Date: 2026-10-29T17:32:53Z
- Venue: cond-mat.str-el, cond-mat.stat-mech, quant-ph
- Authors: Nick G. Jones, Paul Fendley, Nathanan Tantivasadakarn, Ruben Verresen
- Link: https://arxiv.org/abs/2610.40526v1
- Score: 12.0
- Match: 摘要匹配 quantum many-body; 最近 3 天发布

**中文摘要：** 在量子多体相图中，连续的过渡线可以出现然后终止。然而，目前尚不清楚是否可以将相邻状态有意义地描述为类似于水和蒸汽的不同相，因为任何明确的表征都必须超出物质相的通常概念。我们通过引入准相来回答这个问题：临界点附近的有隙状态在更广泛的相图中相连，但不是通过临界理论的小扰动可访问的任何有隙路径。 物理后果包括同一物质相的状态之间的界面模式。更引人注目的是，描述延伸的临界线和连接政权的差距路径需要一个更大的多批判母体理论。在具有中心电荷 $c=1$ 的连续终止线的自旋链示例中，我们发现多临界 $c=3/2$ 和 $c=9/5$ 轨道折叠描述所谓的“商对称保护”和“表示对称保护”拓扑现象。 虽然一维对称保护拓扑相由投影表示类标记，但这些准相可以具有携带更高维线性表示的界面模式。我们通过削弱利布-舒尔茨-马蒂斯异常将其转化为建设性原则。支持不同的准相使得红外临界点成为必要，即使在紫外尺度上它是不必要的。 这种条件比简单地拥有一条余维一临界线更具限制性，它揭示了物质相内比传统分类所暗示的更丰富的结构。
**讨论重点：** 在量子多体相图中，连续的过渡线可以出现然后终止。然而，目前尚不清楚是否可以将相邻状态有意义地描述为类似于水和蒸汽的不同相，因为任何明确的表征都必须超出物质相的通常概念。 结合关键词看，阅读时应重点关注量子多体相关的自由能路径、相稳定性、热力学量的不确定性，以及势函数误差如何传递到宏观性质。
