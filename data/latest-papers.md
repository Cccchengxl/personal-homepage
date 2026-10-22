# Latest papers for 程旭丽

Updated: 2026-10-22T03:00:50.905913+00:00
Window: last 14 days

## 机器学习分子动力学模拟与热力学性质

### 1. Scalable long-range machine learning interatomic potentials with electrical response for atomistic material modeling

- Source: arXiv
- Date: 2026-10-16T15:44:07Z
- Venue: cond-mat.mtrl-sci, cs.LG
- Authors: Yicheng Chen, Xiaoyun Yu, Hyejeong Song, Xintian Wang, Zihui Li, Zixi Xia
- Link: https://arxiv.org/abs/2610.23643v1
- Score: 13.0
- Match: 标题匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 在电场下对材料进行精确的原子模拟需要在长度尺度上进行长程静电和电响应建模，这超出了传统第一原理方法的范围。然而，这些功能仍然难以与机器学习原子间势（MLIP）的可扩展性相协调。严格的局部模型可以实现高效的空间并行化，但忽略了远程交互，而现有的静电扩展引入了阻碍分布式计算的全局依赖性。 在这里，我们通过分析将长程静电力和玻恩有效电荷（BEC）分离为全局静电计算和学习潜电荷的严格局部导数来克服这一限制。该公式保留了等变 MLIP 的空间可分解性，同时能够跨不同边界条件对能量、力、应力和 BEC 进行分布式评估。 该框架在 \texttt{nvalchemi} 平台上以 DPA4C-LR 的形式实现，可在四个 GPU 上扩展到 520 万个原子，其计算成本约为其短程主干的两倍。经过能量和力的训练，DPA4C-LR 可以准确推断 BEC 并再现水的场相关红外光谱。 我们通过恢复弛豫器 \ce{Pb(Mg_{1/3}Nb_{2/3})O3} 特有的微小极化滞后来进一步证明其功能，该滞后在较小的模拟中被有限尺寸效应所掩盖；预测非晶态 \ce{Li_{0.9}NbO_{0.9}Cl_{4.1}} 中室温场驱动离子电导率为 $6.8 \pm 0.7$~mS/cm；并利用平板校正静电对跨硅/金刚石界面的界面热传输进行建模。
**讨论重点：** 严格的局部模型可以实现高效的空间并行化，但忽略了远程交互，而现有的静电扩展引入了阻碍分布式计算的全局依赖性。该框架在 \texttt{nvalchemi} 平台上以 DPA4C-LR 的形式实现，可在四个 GPU 上扩展到 520 万个原子，其计算成本约为其短程主干的两倍。 结合关键词看，阅读时应重点关注机器学习原子间势相关的第一性原理设置、对称性分析、能带或响应函数计算，以及这些量与可观测物性的对应关系。

### 2. Machine Learning-Assisted Discovery of Carbon-Related Defect Formation Mechanisms in Diamond

- Source: arXiv
- Date: 2026-10-19T12:51:02Z
- Venue: cond-mat.mtrl-sci
- Authors: Grace Huang, Christopher Fivecoat, Xun Xu, Mengen Wang
- Link: https://arxiv.org/abs/2610.26301v1
- Score: 12.0
- Match: 摘要匹配 machine learning interatomic potential; 最近 3 天发布

**中文摘要：** 金刚石是固态自旋量子位等功能缺陷的重要主体材料。在通过辐射和随后的热退火产生缺陷的过程中，会产生与碳相关的缺陷，包括空位和填隙，并且可以迁移形成新的缺陷复合体。为了研究这种动力学驱动的过程并揭示中性电荷态双填隙和双空位的形成机制，我们使用密度泛函理论计算生成的小数据集对通用机器学习原子间势进行了微调。 我们获得了单填隙迁移的势垒为 1.84 eV，并发现两个最初分离的单填隙只需克服较低的势垒即可形成双填隙构型。除了训练数据之外，MLIP 还确定了额外的双间隙构型和逐步双空位解离机制的形成途径。这些结果揭示了迁移辅助缺陷复合体形成机制，并证明了有针对性的 MLIP 训练如何识别反应途径。
**讨论重点：** 为了研究这种动力学驱动的过程并揭示中性电荷态双填隙和双空位的形成机制，我们使用密度泛函理论计算生成的小数据集对通用机器学习原子间势进行了微调。在通过辐射和随后的热退火产生缺陷的过程中，会产生与碳相关的缺陷，包括空位和填隙，并且可以迁移形成新的缺陷复合体。 结合关键词看，阅读时应重点关注机器学习原子间势相关的第一性原理设置、对称性分析、能带或响应函数计算，以及这些量与可观测物性的对应关系。

### 3. From Algebraic Completeness to Orbit Separation: Recursive Separating Invariants for Global Neural Network Potential Energy Surfaces

- Source: arXiv
- Date: 2026-10-15T11:20:02Z
- Venue: physics.chem-ph
- Authors: Yiping Hao, Jing Lou, Bina Fu, Dong H. Zhang
- Link: https://arxiv.org/abs/2610.21700v1
- Score: 12.0
- Match: 标题匹配 neural network potential; 近两周发布

**中文摘要：** 置换不变多项式 (PIP) 为全局势能面 (PES) 提供了系统可改进的、保持对称性的表示，但其作为神经网络描述符的高计算成本限制了其在大型分子系统中的应用。基本不变量 (FI) 形成代数完备的生成集，大大减少了描述符的数量，并使神经网络 PES 能够用于更大的系统。然而，随着分子尺寸和复杂性的增加，PES 评估的计算成本仍然很高。 在这里，我们引入了递归分离不变量（RSI），将描述符设计原则从代数完备性转变为轨道分离。 RSI 是通过相关顺序和递归深度系统构建的，提供了计算效率更高的表示。反应性和非反应性系统的基准测试表明，基于 RSI 的神经网络 (RSI-NN) PES 的评估速度比 FI-NN 同类产品快大约一个数量级，并且系统相关的预测精度在多种情况下相当。 这些结果确立了轨道分离作为为全局神经网络 PES 开发有效的对称性保持描述符的有前途的原理。
**讨论重点：** 在这里，我们引入了递归分离不变量（RSI），将描述符设计原则从代数完备性转变为轨道分离。基本不变量 (FI) 形成代数完备的生成集，大大减少了描述符的数量，并使神经网络 PES 能够用于更大的系统。 结合关键词看，阅读时应重点关注神经网络势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 4. Instability-driven segregation of V group transition metals on HEB$_2$ grain boundaries influencing enhanced mechanical properties

- Source: arXiv
- Date: 2026-10-18T14:26:28Z
- Venue: cond-mat.mtrl-sci
- Authors: Daniil Alekseev, Viktor S. Baidyshev, Alexander G. Kvashnin
- Link: https://arxiv.org/abs/2610.25295v1
- Score: 11.0
- Match: 摘要匹配 MACE potential; 最近 3 天发布

**中文摘要：** 五种金属在 (Hf,Ta,Ti,Nb,Zr)B$_2$ (HEB$_2$) 中共享一个公共子晶格。大多数高熵材料都是以烧结陶瓷形式的多晶材料生产的。哪些金属种类位于晶界的问题仍然未知。在这里，我们使用密度泛函理论（DFT）计算了五种二硼化物和HEB$_2$中四种晶界的晶界能$γ_{GB}$。 我们使用 COHP 分析了这些边界处的键合，并使用蒙特卡罗/分子动力学和针对该系统进行微调的 MACE 势，对 HEB$_2$ 的六个边界处的阳离子分离进行了采样（有序和一般）。根据我们的结果$γ_{GB}$按组划分：V族二硼化物NbB$_2$和TaB$_2$在四种GB中的三种中形成了大约IV族能量一半的边界，范围从0.8到2.7，而2.5--4.8~J/m$^2$。 COHP在费米能级上表现出显着差异，即NbB$_2$和TaB$_2$的Me--B键在费米能级($E_F$)处呈反键合，而在GB处成键，而它们的综合强度几乎没有变化。在 HEB$_2$ 中，偏析遵循类似的模式：Nb 和 Ta 在 6 个晶界中的 5 个处富集，包括一般晶界，在 2000~K 时高达 23--35~at.\%，尽管原子的尺寸有利于扩展位点中的 Zr 和 Hf。对于 300~K 的随机边界拉力，偏析的 $Σ193$ 晶界可以承受 26 对 20~GPa 的压力。 HEB$_2$ 的晶界由 V 族金属组成，如二元化合物的边界能及其在费米能级的键合所表明的那样。 (Hf,Ta,Ti,Nb,Zr)B$_2$的晶界优先包括Nb和Ta。这降低了晶界能并强化了晶界。这包括较低的边界能量并改变 NbB$_2$ 和 TaB$_2$ 中的费米能级键合。
**讨论重点：** 五种金属在 (Hf,Ta,Ti,Nb,Zr)B$_2$ (HEB$_2$) 中共享一个公共子晶格。大多数高熵材料都是以烧结陶瓷形式的多晶材料生产的。 结合关键词看，阅读时应重点关注MACE 势函数相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 5. Reticulating Local Dynamics in Three-Dimensional Covalent Organic Frameworks

- Source: arXiv
- Date: 2026-10-17T03:30:37Z
- Venue: cond-mat.mtrl-sci
- Authors: Francesco Tavani, Saber Mirzaei, M. Saeed Mirzaei, Jian Yin, Yen-hsu Lin, Caden Myers
- Link: https://arxiv.org/abs/2610.24418v1
- Score: 10.0
- Match: 摘要匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 在共价有机框架（COF）中，构建单元的几何形状预先决定了框架的结构，但将COF连接体与控制客体吸附和扩散以及机械响应的局部运动相关的可比较的设计原理仍然遥不可及。 在这里，我们将同步加速器 X 射线对分布函数 (PDF) 分析与机器学习原子间势加速的分子动力学 (MD) 模拟相结合，以解析和比较两个三维亚胺连接 COF 的局部动力学，这两个结构单元的几何形状和刚性不同。 两者均由相同的 4 连接的方形平面连接体 $4,4',4'',4'''$-(pyrene-1,3,6,8-tetrayl)tetraaniline (PyTTA) 构成，并与 12 连接的纳米石墨烯六基{[3,5-双($p$-甲酰基苯基)-4,6-二甲氧基苯基]}六苯并晕形成网状COF-412，{[(HBC-LA$_{12}$)(PyTTA)$_3$]}$_{\mathit{imine}}$，并与6-连接的三蝶烯2,3,6,7,14,15-六(4-甲酰基苯基)三蝶烯得到COF-564， {[(Trip-CHO)$_2$(PyTTA)$_3$]}$_{\mathit{亚胺}}$。 PDF-MD方法解析了所有COF连接体运动的幅度、时间尺度和空间范围，将稠合芳族核的有限解放与它们携带的悬垂芳环的较大重新取向倾斜以及网络内整个连接体的平移分开。
**讨论重点：** 在共价有机框架（COF）中，构建单元的几何形状预先决定了框架的结构，但将COF连接体与控制客体吸附和扩散以及机械响应的局部运动相关的可比较的设计原理仍然遥不可及。 在这里，我们将同步加速器 X 射线对分布函数 (PDF) 分析与机器学习原子间势加速的分子动力学 (MD) 模拟相结合，以解析和比较两个三维亚胺连接 COF 的局部动力学，这两个结构单元的几何形状和刚性不同。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 6. Active Learning for Interatomic Potentials: A Review of Uncertainty-Driven Data Efficiency

- Source: arXiv
- Date: 2026-10-16T17:11:07Z
- Venue: physics.comp-ph, cond-mat.mtrl-sci
- Authors: Ilya V. Chepkasov, Alexander V. Shapeev, Alexander G. Kvashnin
- Link: https://arxiv.org/abs/2610.23776v1
- Score: 9.0
- Match: 摘要匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 开发一种机器学习原子间势 (MLIP)，使其能够准确地适应其应用的特定条件，而不仅仅是模型开发人员选择的预定义配置，这是原子模拟中的一项重大挑战。主动学习 (AL) 通过关闭候选生成、数据选择、参考计算和模型更新之间的循环来解决这一挑战。 在这里，我们调查了 70 多项研究，重点关注 2020 年至 2026 年的工作，以了解主动学习如何从针对委员会查询和高斯过程力场的利基动态训练技术演变为多种数据高效策略。他回顾的例子包括动态分子动力学、用于微调预训练模型的主动数据选择、使用冻结预训练模型进行基于内核和表示的采集，以及远离平衡的化学系统的反应感知采样。 我们探索主动学习在元素和合金力学、氢和离子扩散、铁电体和功能材料的有效哈密顿量、反应和光化学动力学、高熵和成分无序材料以及生成和自主材料发现管道中的应用。借鉴越来越多的批判性、方法论上自我意识的文献，我们还表明，这一成就带有系统性的警告。 不确定性估计在模型架构之间不可互换，并且在最重要的地方往往是最不可靠的。最后，我们讨论了基础模型时代标准化、不确定性校准和可观察目标的主动学习工作流程的前景。
**讨论重点：** 我们探索主动学习在元素和合金力学、氢和离子扩散、铁电体和功能材料的有效哈密顿量、反应和光化学动力学、高熵和成分无序材料以及生成和自主材料发现管道中的应用。开发一种机器学习原子间势 (MLIP)，使其能够准确地适应其应用的特定条件，而不仅仅是模型开发人员选择的预定义配置，这是原子模拟中的一项重大挑战。 结合关键词看，阅读时应重点关注机器学习原子间势相关的极化翻转、磁电耦合、自旋-晶格耦合以及多铁序参量之间的相互制约。

### 7. Theoretical Investigation of Oxygen-Vacancy Diffusion in SrTiO$_3$ using Neural Network Potentials

- Source: arXiv
- Date: 2026-10-12T10:10:35Z
- Venue: cond-mat.mtrl-sci
- Authors: Kazutaka Nishiguchi, Ryota Yamamoto, Seiichiro Ten-no
- Link: https://arxiv.org/abs/2610.16521v1
- Score: 9.0
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

### 9. Cluster-based Structural Similarity for Dataset Visualization and Data Selection for Machine Learning Interatomic Potentials

- Source: arXiv
- Date: 2026-09-30T15:41:38Z
- Venue: cond-mat.mtrl-sci
- Authors: Yuto Iwasaki, Miguel A. Caro
- Link: https://arxiv.org/abs/2609.39984v1
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential

**中文摘要：** 机器学习原子间势 (MLIP) 是加速模拟驱动的材料设计的重要组成部分。数据高效的 MLIP 训练依赖于数据选择策略，该策略可最大限度地提高结构多样性，同时限制计算成本高昂的第一性原理计算。这种策略的一个关键挑战是评估结构相似性，这涉及保留单个原子环境的信息和降低计算成本之间的权衡。 在这里，我们提出了同时实现表征保真度和计算效率的相似性评估方法。我们的方法使用由 k-medoids 聚类识别的一小组特征原子环境来表示每个结构，并通过这些代表或其分布之间的最佳匹配来计算成对相似性。分子基准测试表明，我们的方法比基线方法快约 50 倍，同时还可以更清晰地区分具有不同化学成分的结构。 基于相似性的数据选择基准表明，我们的方法提高了 MLIP 中力预测的数据效率和稳定性。
**讨论重点：** 机器学习原子间势 (MLIP) 是加速模拟驱动的材料设计的重要组成部分。我们的方法使用由 k-medoids 聚类识别的一小组特征原子环境来表示每个结构，并通过这些代表或其分布之间的最佳匹配来计算成对相似性。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 10. Sorption Molecular Dynamics of Point Defects in 2D Materials with a Machine Learning Potential

- Source: arXiv
- Date: 2026-10-14T12:04:11Z
- Venue: cond-mat.mtrl-sci
- Authors: Nils-Ruben Skogemyr, Albin Sjöstedt, Isak Wernroth, Isak Häggqvist, Isac Ljungwald, Hans-Ove Åkesson
- Link: https://arxiv.org/abs/2610.20063v1
- Score: 7.0
- Match: 摘要匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 缺陷工程是调整和定制二维 (2D) 材料性能的重要工具。一个关键的挑战是确定哪些缺陷在室温下是动力学稳定的，并且有足够的前景值得进一步研究。然而，使用第一原理计算（例如密度泛函理论（DFT））来识别具有合适特性的稳定缺陷的计算要求很高，有效地限制了高通量研究的范围。 在这项工作中，我们研究了机器学习原子间势 MACE 是否可以重现先前从高通量 DFT 计算中获得的吸附趋势（吸附与吸收），并将分析扩展到高温。使用 MACE 加速分子动力学 (MD) 在 0 K 和 300 K 下模拟了 ADAQ 数据库中总共 17,624 个缺陷结构。结果表明，MACE 成功地重现了 0 K 下 DFT 计算中观察到的总体吸附趋势，而计算成本仅为一小部分。 在 300 K 下进行的模拟进一步表明，当考虑有限温度效应时，定性吸附趋势基本保持不变。这些发现表明，MACE 驱动的 MD 可用作二维材料缺陷相关研究的有效高通量预筛选工具，特别是与吸附相关的研究。虽然传统的第一原理方法（例如 DFT）仍然是准确和定量验证所必需的，但使用 MLIP 可以对有限温度缺陷行为进行 MD 模拟，而计算成本仅为基于 DFT 的 MD 的一小部分。
**讨论重点：** 在这项工作中，我们研究了机器学习原子间势 MACE 是否可以重现先前从高通量 DFT 计算中获得的吸附趋势（吸附与吸收），并将分析扩展到高温。一个关键的挑战是确定哪些缺陷在室温下是动力学稳定的，并且有足够的前景值得进一步研究。 结合关键词看，阅读时应重点关注机器学习原子间势相关的模拟体系、时间尺度、温度条件、动力学稳定性，以及有限温度性质对势函数质量的敏感性。

## 凝聚态物理强关联体系和多铁性质

### 1. Ballistic transport and crystallographic control in altermagnetic quantum rings

- Source: arXiv
- Date: 2026-10-19T19:08:28Z
- Venue: cond-mat.mes-hall
- Authors: Edilberto O. Silva
- Link: https://arxiv.org/abs/2610.27173v1
- Score: 23.0
- Match: 标题匹配 altermagnetic; 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 我们研究通过具有非磁性引线的有限宽度 $d$ 波交变磁量子环的相干两端传输。受限的阿哈罗诺夫-玻姆通量保持精确的 $h/e$ 周期性，并且在对称单模几何结构中，产生精确的半通量传输零。垂直场根据有效面积 $A_{\rm eff}=1.0342\,πr_0^2$ 移动干涉图案，并且交变磁分裂将公共零解析为附近的自旋相关节点。旋转晶体会反转传输的自旋，而镜子方向 $θ_A=π/4$ 恰好是自旋简并。 对于 $50$~nm 参考环，亚特斯拉场产生 $|P_T|>0.99$ 的窗口，其中最容易获得的窗口需要单独的均匀场并且没有受限通量。有限偏置、热、无序、塞曼和自旋守恒电压探针计算表明，极化明显比单个相干共振振幅更稳定。这些结果将干涉节点位置、通量周期性和晶体控制的自旋极化确定为交变介观干涉仪在实验上有用的特征。
**讨论重点：** 我们研究通过具有非磁性引线的有限宽度 $d$ 波交变磁量子环的相干两端传输。受限的阿哈罗诺夫-玻姆通量保持精确的 $h/e$ 周期性，并且在对称单模几何结构中，产生精确的半通量传输零。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 2. Microscopic origin of field-induced multiferroicity in Ni3TeO6

- Source: arXiv
- Date: 2026-10-21T08:45:40Z
- Venue: cond-mat.mtrl-sci
- Authors: J. Lass, R. Toft-Petersen, A. A. Turrini, Ø. S. Fjellvåg, B. Decrausaz, K. M. L. Krighaar
- Link: https://arxiv.org/abs/2610.29420v1
- Score: 21.0
- Match: 标题匹配 multiferroic; 摘要匹配 multiferroic materials; 最近 3 天发布

**中文摘要：** 对更小、更快、更节能技术的持续需求推动了凝聚态物质研究转向在单相内结合多种响应的材料。特别有趣的例子是具有有序参数之间交叉耦合的多铁性材料。 Ni3TeO6 是此类材料的重要成员，在磁场下表现出无磁滞转变，同时影响磁结构、电极化和声子频率。 在这里，我们结合中子散射技术揭示了这种多铁性转变的微观起源。我们确定了有限 Dzyaloshinskii-Moriya 交换项的存在，该交换项产生了在磁场中软化的非互易手性自旋波。它们的凝结改变了控制电极化并驱动离子位移的磁性结构，从而耦合了磁、电和晶格自由度。 我们的研究表明，中子散射是一种强大的技术，可以阐明多铁材料中的微观相互作用，为下一代电子设备的设计提供信息。
**讨论重点：** 我们的研究表明，中子散射是一种强大的技术，可以阐明多铁材料中的微观相互作用，为下一代电子设备的设计提供信息。特别有趣的例子是具有有序参数之间交叉耦合的多铁性材料。 结合关键词看，阅读时应重点关注多铁性、多铁材料相关的极化翻转、磁电耦合、自旋-晶格耦合以及多铁序参量之间的相互制约。

### 3. Projective symmetry groups beyond spin-$1/2$: Classifying integer-spin quantum spin liquids

- Source: arXiv
- Date: 2026-10-21T17:08:50Z
- Venue: cond-mat.str-el
- Authors: Atanu Maity, Chunxiao Liu, Rhine Samajdar, Yasir Iqbal
- Link: https://arxiv.org/abs/2610.30048v1
- Score: 18.0
- Match: 标题匹配 quantum spin liquid; 最近 3 天发布

**中文摘要：** Wen 的射影对称群 (PSG) 在 25 年前提出，将对称量子自旋液体的分类简化为代数问题，并从此指导了自旋 $1/2$ 模型和材料的研究。然而，当前许多候选材料和量子模拟器都具有 1 美元或更大的自旋矩，并且不存在可比的分类。我们制定了任意自旋$S$的费米子部分子的PSG。整数和半奇整数自旋的规范结构已经不同。 半奇整数自旋给出了熟悉的 $\mathrm{SU}(2)$、$\mathrm{U}(1)$ 和 $\mathbb{Z}_2$ 不变规范组，而整数自旋给出了不同的层次结构，包括 $\mathrm{U}(1)\rtimes\mathbb{Z}_2$ 和 $\mathbb{Z}_2\times\mathbb{Z}_2$；后者没有 spin-$1/2$ 对应物。对于整数自旋，三个与晶格无关的结果如下。在位点交换下，部分子的单线态配对是奇怪的。晶格对称性可以交换局部约束的粒子和孔表示，这迫使对称相关的位点进入相反的约束扇区。 仅当每个晶胞的位点数量是 $2S+1$ 的倍数时，每个位点具有相同约束的时间反转对称 $\mathrm{U}(1)$ 状态才能有间隙。我们将形式主义应用于自旋 $1$ 金刚石晶格，在受挫的 A 位尖晶石中实现，并找到十个完全对称的 Ansätze 直到第二个邻居。在平均场水平的 $J_1$-$J_2$ 海森堡模型中，基态取决于如何施加约束。 对于粒子和空穴表示，最低状态是完全有间隙的 $\mathrm{U}(1)$ 状态，其两个子晶格位于相反的约束扇区，其中一个子晶格的规范相当于一对 Ansatz。该分类为其他晶格和其他材料中的整数自旋量子自旋液体提供了一个起点。
**讨论重点：** Wen 的射影对称群 (PSG) 在 25 年前提出，将对称量子自旋液体的分类简化为代数问题，并从此指导了自旋 $1/2$ 模型和材料的研究。在平均场水平的 $J_1$-$J_2$ 海森堡模型中，基态取决于如何施加约束。 结合关键词看，阅读时应重点关注量子自旋液体相关的新方法的假设、训练或计算流程、适用体系，以及与已有方法相比的优势和局限。

### 4. Stabilizing and detecting electron fractionalization in the Hofstadter-Hubbard model

- Source: arXiv
- Date: 2026-10-21T15:55:01Z
- Venue: cond-mat.str-el, cond-mat.mes-hall, cond-mat.mtrl-sci
- Authors: Jiahao Yang, Zeyu Han, Gang v. Chen
- Link: https://arxiv.org/abs/2610.29916v1
- Score: 18.0
- Match: 标题匹配 Hubbard model; 最近 3 天发布

**中文摘要：** 受莫尔系统中相关陈绝缘体物理最新进展的推动，我们研究了半填充三角晶格 Hofstadter-Hubbard 模型及其电子分裂。在各种竞争的非磁性状态中，增加轨道通量可以稳定并拓宽莫特体系中的 $\mathrm{U}(1)_2$ 手性自旋液相。在这种奇异的状态下，电子被分成有隙自旋子和有隙电荷，其有效能带与轨道通量相关。 窄自旋子带与带隙电荷激发的卷积在电子谱函数和态密度中产生丰富且可辨别的结构。这些结果不仅将轨道通量确定为电子分裂详细模式和莫特跃迁性质的控制参数，而且还为相关系统的角分辨光发射和扫描隧道研究提供了关键的光谱特征，将自由粒子能带拓扑与相关区域中的固有拓扑顺序联系起来。
**讨论重点：** 受莫尔系统中相关陈绝缘体物理最新进展的推动，我们研究了半填充三角晶格 Hofstadter-Hubbard 模型及其电子分裂。在各种竞争的非磁性状态中，增加轨道通量可以稳定并拓宽莫特体系中的 $\mathrm{U}(1)_2$ 手性自旋液相。 结合关键词看，阅读时应重点关注Hubbard 模型相关的有效模型参数、电子关联强度、相图边界以及可与实验对照的谱学或输运信号。

### 5. Quantics tensor trains for multiloop functional renormalization group in multiorbital impurity models

- Source: arXiv
- Date: 2026-10-21T07:36:41Z
- Venue: cond-mat.str-el
- Authors: Hyun-Yong Lee, Naoki Kawashima
- Link: https://arxiv.org/abs/2610.29341v1
- Score: 17.0
- Match: 摘要匹配 altermagnetic; 摘要匹配 altermagnet; 最近 3 天发布

**中文摘要：** 电子相互作用的完全频率依赖性是动态相关性的核心，但其数值成本限制了多轨道计算。我们直接在量子张量序列表示中制定多循环函数重整化群，在广泛的范围内保留所有三个独立的顶点频率，而无需显式的高频参数化。分析张量运算符执行频率变换和内部求和，无需密集顶点中间值。 多环校正提高了顶点和响应与独立参考的一致性，并再现了低能量数值重正化群自能。较低温度计算解决了二次频率对分析连续散射率的影响。简并二轨道杂质在固定亨德耦合下表现出独特的自旋、轨道和电荷响应。在补偿交变磁环境中，尽管未受干扰的杂质的磁化强度为零，但轨道能级分裂仍会引起局部自旋响应。 增加亨德耦合会抑制轨道响应，同时增加其自旋极化。单独重整化的单粒子传播并不能重现这种强烈的偏振依赖性。这些结果将压缩多环计算扩展到多轨道环境中的动态相关性。
**讨论重点：** 电子相互作用的完全频率依赖性是动态相关性的核心，但其数值成本限制了多轨道计算。我们直接在量子张量序列表示中制定多循环函数重整化群，在广泛的范围内保留所有三个独立的顶点频率，而无需显式的高频参数化。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 6. Spin fluctuations and nearly isotropic quasiparticles in the doped three-dimensional Hubbard model

- Source: arXiv
- Date: 2026-10-20T07:45:59Z
- Venue: cond-mat.str-el
- Authors: Pengcheng Hou, Kun Chen, Youjin Deng
- Link: https://arxiv.org/abs/2610.27779v1
- Score: 17.0
- Match: 标题匹配 Hubbard model; 最近 3 天发布

**中文摘要：** 远离半填充且高于尼尔温度，三维哈伯德模型是一种具有反铁磁自旋涨落的顺磁性金属，其中缺乏受控动量解析结果。使用连通行列式蒙特卡罗图，我们计算了 n = 0.4-0.95、T/t = 0.05-0.33 和 U/t = 4-8 的动量分辨自能，以及其中 12 个点的全区自旋敏感性，重点关注 U/t = 4。 在 U/t = 4 和接近半填充时，自旋波动变得更强：对于 n = 0.7-0.9，在 T/t = 0.14 时，它们将磁化率峰值增强至七倍，并将散射率的动量相关部分提高至其二阶值的四到五倍。它们由有效的自旋相互作用驱动，该自旋相互作用筛选至约 2U/3 并且在整个区域上几乎均匀。然而，峰值高度是由峰值波矢量处的这种相互作用的稍小的值决定的，并且在磁阶附近，这种微小的差异会以很大的系数改变高度。 双粒子自洽理论再现了峰值，因为它的求和规则将其单一常数相互作用固定在该值附近，但对于 n = 0.7-0.9，T/t = 0.14，其自能高估了局部散射率并低估了动量相关部分。虽然波动很强，但波动范围很短，相关长度最多约为两个晶格间距，并且对于 n = 0.7-0.9 且 T/t >= 0.14，费米表面附近的散射率在固定带能量下最多变化约 1%，没有热点。 当 U/t = 4 时，动态平均场理论 (DMFT) 在百分之几内重现了局部散射率和准粒子重量，并且它错过的非局部部分大约是能带能量的函数。因此，强自旋涨落与近各向同性准粒子共存，其结果为 DMFT 的扩展和自旋涨落理论提供了基准。
**讨论重点：** 因此，强自旋涨落与近各向同性准粒子共存，其结果为 DMFT 的扩展和自旋涨落理论提供了基准。远离半填充且高于尼尔温度，三维哈伯德模型是一种具有反铁磁自旋涨落的顺磁性金属，其中缺乏受控动量解析结果。 结合关键词看，阅读时应重点关注Hubbard 模型相关的有效模型参数、电子关联强度、相图边界以及可与实验对照的谱学或输运信号。

### 7. Acceleration of CTQMC via Denoising Diffusion Models with Auxiliary Spectral Functions

- Source: arXiv
- Date: 2026-10-20T17:11:41Z
- Venue: cond-mat.str-el
- Authors: Rishi Rao, Li Zhu
- Link: https://arxiv.org/abs/2610.28542v1
- Score: 16.0
- Match: 摘要匹配 Hubbard model; 摘要匹配 dynamical mean field theory; 最近 3 天发布

**中文摘要：** 连续时间量子蒙特卡罗 (CTQMC) 杂质求解器是求解动态平均场理论 (DMFT) 方程的数值精确但昂贵的选择，欠采样产生的统计噪声给低温研究带来了重大挑战。这种噪声在采样的自能中尤其严重，在插入戴森方程时可能会破坏自洽环的稳定性。在这项工作中，我们基于在合成数据上训练的扩散模型架构，引入了费米子虚数时间格林函数的神经降噪器。 该网络预测与噪声虚轴 CTQMC 数据一致的正和归一化辅助谱函数，然后通过自微分进行细化，以匹配测量的自能、前两个高频矩以及类似于约束残差最小化 (CRM) 方法的杂质占据。这导致了格林函数和自能是设计上的因果关系。通过这个去噪框架，我们能够将所需的 CTQMC 测量步骤减少 10-100 倍。 我们使用 Bethe 晶格上的半填充 Hubbard 模型、二维 Hubbard 模型的两面片动态聚类近似 (DCA) 以及 SrVO$_3$ 系统对我们的方法进行基准测试。我们通过仅 5000 个 CTQMC 测量的半填充 Hubbard 模型在增加库仑相互作用时重现莫特跃迁，仅用 5$\times$10$^5$ 测量的 DCA 二维 Hubbard 模型的赝能隙跃迁，并以比参考少 50 倍的测量来匹配 SrVO$_3$ 的谱函数。 由于我们生成辅助谱函数，因此我们可以免费恢复系统的近似谱函数，而无需执行解析延拓。
**讨论重点：** 在这项工作中，我们基于在合成数据上训练的扩散模型架构，引入了费米子虚数时间格林函数的神经降噪器。我们使用 Bethe 晶格上的半填充 Hubbard 模型、二维 Hubbard 模型的两面片动态聚类近似 (DCA) 以及 SrVO$_3$ 系统对我们的方法进行基准测试。 结合关键词看，阅读时应重点关注Hubbard 模型、动力学平均场理论相关的有效模型参数、电子关联强度、相图边界以及可与实验对照的谱学或输运信号。

### 8. Robust Anomalous Hall Effect in Epitaxial Cubic D0$_3$-Fe$_3$Ge Nanoplates Grown by Chemical Vapor Deposition

- Source: arXiv
- Date: 2026-10-21T15:15:37Z
- Venue: cond-mat.mtrl-sci
- Authors: Mingxuan Chen, Chao Chen, Siqi Jiang, Shuxiang Qiao, Hongyan Lu, Di Zhang
- Link: https://arxiv.org/abs/2610.29858v1
- Score: 14.0
- Match: 摘要匹配 ferromagnetism; 最近 3 天发布

**中文摘要：** 铁基铁磁材料由于其高居里温度和由贝里曲率驱动的显着反常霍尔效应（AHE）而成为自旋电子学的有前途的系统。尽管人们对非层状铁基铁磁材料的外延生长进行了研究，但高质量单晶薄膜的实现仍然是一个巨大的障碍。同时，晶界散射等问题进一步阻碍了它们的表征和应用。 在这里，我们报告了单晶立方 D0$_3$-Fe$_3$Ge 纳米板的首次化学气相沉积 (CVD) 合成。这种化合物与 Fe-Ge 系统中通常观察到的传统六方相有很大不同。结构表征证实了晶体的立方晶格和化学计量纯度。结构分析发现了强烈的外延效应，导致界面处产生约 4.16% 的巨大压缩应变，并逐渐向表面松弛。 二次谐波产生（SHG）信号可能进一步揭示这种界面应变破坏了立方相固有的中心对称性。 SQUID 磁力测量显示出强大的室温铁磁性和明显的磁各向异性。磁输运测量揭示了强大的 AHE，在远超过室温的温度下仍保持稳定。在反常霍尔电阻和纵向电阻之间观察到的缩放强烈表明这种效应是由固有的贝里曲率机制主导的。 此外，密度泛函理论（DFT）计算表明，巨大的外延应变会引起能带重建，并在费米能级附近产生密集的自旋轨道耦合间隙，有效地使反常霍尔电导率加倍，以匹配我们的实验观察结果。
**讨论重点：** 铁基铁磁材料由于其高居里温度和由贝里曲率驱动的显着反常霍尔效应（AHE）而成为自旋电子学的有前途的系统。尽管人们对非层状铁基铁磁材料的外延生长进行了研究，但高质量单晶薄膜的实现仍然是一个巨大的障碍。 结合关键词看，阅读时应重点关注铁磁性相关的第一性原理设置、对称性分析、能带或响应函数计算，以及这些量与可观测物性的对应关系。

### 9. Interaction-Induced Bloch Geometry and Transverse Thermoelectric Transport

- Source: arXiv
- Date: 2026-10-21T09:42:14Z
- Venue: cond-mat.mes-hall
- Authors: Heng-Yu Di, YuanDong Wang, Zhen-Gang Zhu, Gang Su
- Link: https://arxiv.org/abs/2610.29486v1
- Score: 14.0
- Match: 摘要匹配 Hubbard model; 最近 3 天发布

**中文摘要：** 电子-电子相互作用可以重建布洛赫波函数，改变它们的几何形状和相关的热电响应。我们使用热长度规范密度矩阵方法推导出 Hartree--Fock (HF) 近似内的线性热电响应，解决了 Drude、对称量子度量和反对称 Berry 曲率贡献。在非交互的 Bloch 特征基中，我们将重建的 Berry 连接分为非交互连接和交互连接。 这为异常热电响应提供了裸露、相干和相互作用连接的贡献。我们确定空间反转、旋转、时间反转和组合对称性对三个传输通道施加的约束。在弛豫时间近似中，主要的弱展宽行为是 Drude 贡献的 $Г^{-1}$、量子度量贡献的 $Г$ 和 Berry 曲率贡献的 $Г^0$。带间缩放适用于远离带简并性的情况。 三角晶格扩展哈伯德模型的自洽计算说明了相互作用如何产生贝里曲率和量子度量，改变系统的对称性，从而有助于横向热电传输。
**讨论重点：** 我们使用热长度规范密度矩阵方法推导出 Hartree--Fock (HF) 近似内的线性热电响应，解决了 Drude、对称量子度量和反对称 Berry 曲率贡献。在非交互的 Bloch 特征基中，我们将重建的 Berry 连接分为非交互连接和交互连接。 结合关键词看，阅读时应重点关注Hubbard 模型相关的有效模型参数、电子关联强度、相图边界以及可与实验对照的谱学或输运信号。

### 10. Disorder-Mediated Magnetism in Transition-Metal Dichalcogenide Monolayers: XS$_2$ and XSe$_2$ (X = Ti, V, Co, Mo, and Ru)

- Source: arXiv
- Date: 2026-10-21T05:44:16Z
- Venue: cond-mat.mtrl-sci
- Authors: Chi-Cheng Lee, Yukiko Yamada-Takamura, Taisuke Ozaki
- Link: https://arxiv.org/abs/2610.29235v1
- Score: 14.0
- Match: 摘要匹配 ferromagnetism; 最近 3 天发布

**中文摘要：** 过渡金属二硫属化物单层中的磁性引起了相当大的关注，但其性质仍然难以捉摸，特别是在单层 1T-VSe$_2$ 中。我们的第一原理计算表明，斯托纳不稳定性可以驱动 XS$_2$ 和 XSe$_2$ 单层（X = Ti、V、Co、Mo 和 Ru）中的铁磁性，与费米能级态密度的降低相关。我们证明，混合非磁性钛、钴、钼和钌二硫化物或二硒化物可以产生磁性。相反，将磁性VS$_2$或VSe$_2$与其他化合物混合可以完全抑制磁性。 两种情况都可以降低总能量。此外，用Co缺陷取代少量V原子也可以破坏1T-V(S,Se)$_2$中的铁磁性。即使在原始的 1T-VSe$_2$ 中，我们也发现了具有反向局部 V 矩的亚铁磁结构，这些结构几乎随着铁磁态而退化。它们的竞争可能有助于抑制长程铁磁有序。磁性和结构无序的能量损失减少是由于费米能级的态密度受到抑制，类似于佩尔斯转变的机制。 因此，电子驱动的能量降低到费米能级附近可能在各种形式的过渡金属二硫属化物单层中广泛存在。
**讨论重点：** 过渡金属二硫属化物单层中的磁性引起了相当大的关注，但其性质仍然难以捉摸，特别是在单层 1T-VSe$_2$ 中。我们的第一原理计算表明，斯托纳不稳定性可以驱动 XS$_2$ 和 XSe$_2$ 单层（X = Ti、V、Co、Mo 和 Ru）中的铁磁性，与费米能级态密度的降低相关。 结合关键词看，阅读时应重点关注铁磁性相关的第一性原理设置、对称性分析、能带或响应函数计算，以及这些量与可观测物性的对应关系。
