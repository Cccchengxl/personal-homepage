# Latest papers for 程旭丽

Updated: 2026-11-07T04:17:28.563704+00:00
Window: last 14 days

## Notes

- arXiv query failed for 机器学习分子动力学模拟与热力学性质: The read operation timed out
- 机器学习分子动力学模拟与热力学性质 kept previous papers because the current query returned 0 results.
- arXiv query failed for 凝聚态物理强关联体系和多铁性质: The read operation timed out
- 凝聚态物理强关联体系和多铁性质 kept previous papers because the current query returned 0 results.

## 机器学习分子动力学模拟与热力学性质

### 1. Machine-Learning Molecular Dynamics Reveals Grotthuss Transport in Concentrated Electrolytes

- Source: arXiv
- Date: 2026-11-03T09:24:13Z
- Venue: physics.chem-ph, cond-mat.other
- Authors: Øystein Gullbrekken, Sondre Kvalvåg Schnell
- Link: https://arxiv.org/abs/2611.04558v1
- Score: 12.0
- Match: 摘要匹配 machine learning interatomic potential; 最近 3 天发布

**中文摘要：** 质子转移是酸性或碱性水溶液中异常高电导率的原因。然而，质子转移机制对浓水溶液电导率的贡献尚不清楚。在这项工作中，我们使用分子动力学模拟和机器学习原子间势 (MLIP)（包括质子转移）来计算不同浓度的 KOH(aq) 系统的输运特性。 我们量化了质子转移机制对氢氧根离子和水分子扩散性以及电解质的离子电导率和传输数的贡献。在较低浓度下，贡献很大，但在浓度非常高时，贡献会减弱。
**讨论重点：** 质子转移是酸性或碱性水溶液中异常高电导率的原因。然而，质子转移机制对浓水溶液电导率的贡献尚不清楚。 结合关键词看，阅读时应重点关注机器学习原子间势相关的模拟体系、时间尺度、温度条件、动力学稳定性，以及有限温度性质对势函数质量的敏感性。

### 2. A Hybrid Message-Passing and Electric-Field Representation for Electrostatic QM/MM Embedding with Machine Learning Interatomic Potentials

- Source: arXiv
- Date: 2026-10-30T10:16:32Z
- Venue: physics.chem-ph, physics.bio-ph, physics.comp-ph
- Authors: Raphael T. Husistein, Shobhit S. Chaturvedi, Thomas Weymuth, Beatriz Piniello, Sélène Forget, Kresten Lindorff-Larsen
- Link: https://arxiv.org/abs/2610.41523v1
- Score: 12.0
- Match: 标题匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 在混合量子力学/分子力学方法中，大型原子系统的一小部分区域通过量子力学进行描述，而系统的其余部分则由经典力场表示。尽管如此，量子计算的计算成本严重限制了可实现的模拟和采样时间。用在量子参考数据上训练的机器学习原子间势（MLIP）代替量子计算可以大大增加可用的模拟时间。 然而，准确性和效率很大程度上取决于 MLIP 结合经典（静电）环境信息的具体方式。在这里，我们证明了纯粹基于外部电场衍生特征的现有策略无法区分某些环境，最终限制了其准确性。 作为解决方案，我们提出了对等变 TensorNet 架构的扩展，通过将靠近量子区域的经典原子合并到消息传递方案中，并结合从电场导出的特征来描述更远的环境，从而减轻了这一缺点。我们证明，这种组合比单独使用任何一种方法都能实现更高的准确性。
**讨论重点：** 作为解决方案，我们提出了对等变 TensorNet 架构的扩展，通过将靠近量子区域的经典原子合并到消息传递方案中，并结合从电场导出的特征来描述更远的环境，从而减轻了这一缺点。在混合量子力学/分子力学方法中，大型原子系统的一小部分区域通过量子力学进行描述，而系统的其余部分则由经典力场表示。 结合关键词看，阅读时应重点关注机器学习原子间势相关的新方法的假设、训练或计算流程、适用体系，以及与已有方法相比的优势和局限。

### 3. Does System Size Matter in Uncertainty Quantification for Machine Learning Interatomic Potentials?

- Source: arXiv
- Date: 2026-10-29T14:20:35Z
- Venue: cs.LG, cond-mat.mtrl-sci
- Authors: Chayaphol Lortaraprasert, Nontawat Charoenphakdee, Wenwen Li, Yong-Bin Zhuang, Yuta Tsuboi
- Link: https://arxiv.org/abs/2610.40126v1
- Score: 11.0
- Match: 标题匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 机器学习原子间势 (MLIP) 通常使用不确定性估计来标记分布外 (OOD) 配置并选择主动学习的结构。一个关键问题是，所得的结构级不确定性分数在不同系统规模之间是否保持可比性。常见的做法是通过平均值或最大值来聚合每个原子的不确定性，并将所得分数与固定阈值进行比较，隐含地假设这种可比性。 我们通过将两个聚合表征为原子计数的函数，在几个分布内 (ID)/OOD 对上测试了这一假设。这两个聚合表现出不同的大小依赖性。对于同质系统，平均聚集仍然与尺寸无关，但失去了对大细胞缺陷的敏感性。相比之下，ID 系统的最大聚合随着系统规模的增长而增长，而对于包含缺陷的系统则保持大致平坦，以与极值统计一致的方式缩小 ID-OOD 差距。 尽管大型结构中高度不确定的原子可能表明新的局部环境，但与在训练分布之外构造的 OOD 结构上的再训练相比，对这些结构的再训练几乎没有带来什么改善。我们的结果揭示了尺寸感知不确定性标准的实际局限性，并激发了尺寸感知校准，以在大规模原子模拟中实现更可靠的 OOD 检测。
**讨论重点：** 机器学习原子间势 (MLIP) 通常使用不确定性估计来标记分布外 (OOD) 配置并选择主动学习的结构。一个关键问题是，所得的结构级不确定性分数在不同系统规模之间是否保持可比性。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 4. Distilling Large-Scale Machine Learning Interatomic Potentials to Predict Long-Timescale Electrolyte Transport Properties

- Source: arXiv
- Date: 2026-10-29T07:12:15Z
- Venue: physics.chem-ph, cond-mat.mtrl-sci, cond-mat.soft
- Authors: Ishan Amin, Yue Jian, Nitesh Kumar, Christine Zhang, Jianwei Lai, Casey S. Mezerkor
- Link: https://arxiv.org/abs/2610.39513v1
- Score: 11.0
- Match: 标题匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 准确预测液体电解质的传输特性对于下一代电池设计至关重要，并且需要量子力学精确且足够快的力场以进行长时间尺度的模拟。最近的大规模预训练机器学习原子间势（MLIP）接近密度泛函理论的准确性，但仍然太慢，无法获得收敛传输特性所需的时间尺度。 我们提供知识蒸馏程序，将大规模“教师”MLIP 的准确性转移到快速、特定于系统的“学生”，而无需任何额外的从头开始数据。我们的精炼模型运行速度快了约 40 倍，再现了教师预测的结构可观测值，并在几天内生成稳定的 20 ns 轨迹，而不是教师要求的几个月。 在各种钠离子和锂离子电解质中，学生预测的自扩散率、离子电导率和剪切粘度跟踪实验并优于经典力场预测，将蒸馏确立为高通量电解质筛选所需的精确、长时间尺度模拟的实用途径。
**讨论重点：** 准确预测液体电解质的传输特性对于下一代电池设计至关重要，并且需要量子力学精确且足够快的力场以进行长时间尺度的模拟。最近的大规模预训练机器学习原子间势（MLIP）接近密度泛函理论的准确性，但仍然太慢，无法获得收敛传输特性所需的时间尺度。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 5. Learning Between the Lines: Interaction Interpolation in a Multi Element Machine Learning Interatomic Potential

- Source: arXiv
- Date: 2026-10-28T20:45:15Z
- Venue: cond-mat.mtrl-sci
- Authors: Ademola Soyemi, Kipton Barros, Timothy C. Germann, Benjamin T. Nebgen, Brenden W. Hamilton
- Link: https://arxiv.org/abs/2610.38876v1
- Score: 10.0
- Match: 标题匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 近年来，机器学习原子间势（MLIAP）的不断发展极大地加速了材料研究。然而，为每个独特问题构建定制 MLIAP 的需求仍然是一个瓶颈，这引发了 MLIAP 的可转移性问题。虽然基础 MLIAP 由于其训练集中所代表的化学空间的广泛覆盖而可以实现可转移性，但它们的大小和计算成本限制了它们的常规使用。 我们通过开发一种适用于十二种元素（Al、Sc、Ti、V、Cu、Zn、Zr、Nb、Mo、Hf、Ta、W）金属合金的轻质通用 MLIAP 来解决这一差距。在这里，我们利用逐步主动学习（AL）方法来开发一个紧凑而多样化的数据集和模型，通过从以前看到的交互中进行插值来很好地概括。由此产生的电势有效地转移到看不见的、更高体序的合金系统，只需要一元和二元训练数据来捕获三元和四元系统。 该模型还通过网络内的炼金术外推法很好地转移到新元素，只需要新元素及其合金的一元数据。这些发现表明，在有针对性的、多样性驱动的数据集上训练的 MLIAP 以相对较低的计算成本提供可转移性，为实现通用、资源高效的材料建模 MLIAP 提供了一条实用途径。
**讨论重点：** 在这里，我们利用逐步主动学习（AL）方法来开发一个紧凑而多样化的数据集和模型，通过从以前看到的交互中进行插值来很好地概括。然而，为每个独特问题构建定制 MLIAP 的需求仍然是一个瓶颈，这引发了 MLIAP 的可转移性问题。 结合关键词看，阅读时应重点关注机器学习原子间势相关的新方法的假设、训练或计算流程、适用体系，以及与已有方法相比的优势和局限。

### 6. PLUMED-JAX: GPU-native enhanced sampling for atomistic simulations

- Source: arXiv
- Date: 2026-10-31T00:15:58Z
- Venue: physics.chem-ph
- Authors: Venkat Kapil
- Link: https://arxiv.org/abs/2611.00483v1
- Score: 8.0
- Match: 摘要匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 我们提出了 PLUMED-JAX，它是一种人工智能辅助的适应系统，对选定的 PLUMED 集体变量、伞式采样和元动力学进行基于 JAX 的原子模拟，使用 gpt-6.1-sol 开发，并在 Codex 工具中将推理工作设置为高。与 JAX-MD 集成支持编译的分子动力学、批量复制、共享偏差的步行器以及跨多个图形处理单元的执行。 我们根据 PLUMED 和精确的自由能基准验证了该框架，并演示了在丁烷、硅结晶和锂传输中的应用，经典力场和机器学习原子间势的计算吞吐量均得到了数倍的提高。
**讨论重点：** 我们提出了 PLUMED-JAX，它是一种人工智能辅助的适应系统，对选定的 PLUMED 集体变量、伞式采样和元动力学进行基于 JAX 的原子模拟，使用 gpt-6.1-sol 开发，并在 Codex 工具中将推理工作设置为高。我们根据 PLUMED 和精确的自由能基准验证了该框架，并演示了在丁烷、硅结晶和锂传输中的应用，经典力场和机器学习原子间势的计算吞吐量均得到了数倍的提高。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 7. Retention-constrained fine-tuning of a pre-trained aluminium MACE potential for non-equilibrium defect dynamics and plasticity

- Source: arXiv
- Date: 2026-10-26T16:00:16Z
- Venue: cond-mat.mtrl-sci
- Authors: Yue Wu, Yuan Tian, Deng Pan, Mingwei Chen
- Link: https://arxiv.org/abs/2610.35653v1
- Score: 8.0
- Match: 标题匹配 MACE potential; 近两周发布

**中文摘要：** 针对非平衡缺陷动力学和塑性调整预先训练的机器学习原子间势需要在不降低近平衡弹性和振动响应的情况下提高缺陷精度。在这里，我们通过集成条件读数不确定性、迭代全参数更新和协议兼容的相对能量锚定来实现铝 MACE 势 QP17 的平衡。超过 144 个线性读出权重的灵敏度指导采集，并具有批内协方差更新和不断发展的神经表示。 经过四轮主动学习（32 次获取配置和 400 次梯度更新）后，力不确定性获取将平均开发力误差从 22.43 减少到 21.52 meV/Angstrom，在相同更新预算下优于随机采样 (22.70)、几何多样性选择 (22.46) 和所有 104 个候选标签 (22.71) 的统一训练。所有三个力不确定度运行都满足体机械保留标准：历史相对能量误差从 0.375 meV/atom 减少到 0.207 meV/atom，而谐波声子均方根漂移保持在 0.05 THz 以下。 匹配的客观消融表明相对能量锚定抑制谐波漂移。跨平面断层、孪晶界和晶界的样本外评估表明，即使从未拟合维里应力，缺陷能量和偏应力也可转移。闭环分子动力学和密度泛函理论 (MD-DFT) 试验证实，自动接受门控会拦截违反历史弹性群能量或振动容差的更新。 这些组件共同建立了一个保留约束的微调协议，用于改善塑性变形可观测值，同时保留测试的整体机械响应。
**讨论重点：** 针对非平衡缺陷动力学和塑性调整预先训练的机器学习原子间势需要在不降低近平衡弹性和振动响应的情况下提高缺陷精度。在这里，我们通过集成条件读数不确定性、迭代全参数更新和协议兼容的相对能量锚定来实现铝 MACE 势 QP17 的平衡。 结合关键词看，阅读时应重点关注MACE 势函数相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 8. A thermodynamic correction layer for machine learning interatomic potentials

- Source: arXiv
- Date: 2026-10-25T20:26:05Z
- Venue: cond-mat.mtrl-sci
- Authors: Sarath Menon, Braulio Sanchez Ortega, Ralf Drautz
- Link: https://arxiv.org/abs/2610.34551v1
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 机器学习原子间势能在大长度和时间尺度上以接近 \textit{ab initio} 的精度实现原子模拟。基础模型将这种能力扩展到整个元素周期表，但继承了用于生成训练数据的电子结构方法的热力学描述。因此，相对相位稳定性的小误差可能会导致转变温度的大误差。 我们引入了附加热力学校正层，该层可将相自由能移向评估参考，而无需重新训练或修改基础电势。一阶热力学结构将所需的相自由能位移直接转换为构型能量目标，该目标使用线性原子团簇展开进行拟合，并根据测量的自由能迭代细化。我们使用基础 GRACE 模型将该方法应用于具有不同晶体结构的元素之间的熔化和固体到固体的转变。 校正后，所有转变温度均位于评估值的规定公差范围内，包括 Ca、Ti 和 Zr，其中固相转变和熔化一起校正。静态能量曲线、体积模量和液体结构仍然接近基础模型。空位形成能、热膨胀和液体密度取决于校正后的相平衡以及校正较大时的变化。该方法既不需要再训练、可微分动力学，也不需要访问基础势的参数。 它提供了一种将可转移原子模型与评估相热力学相结合的模块化途径。
**讨论重点：** 我们引入了附加热力学校正层，该层可将相自由能移向评估参考，而无需重新训练或修改基础电势。我们使用基础 GRACE 模型将该方法应用于具有不同晶体结构的元素之间的熔化和固体到固体的转变。 结合关键词看，阅读时应重点关注机器学习原子间势相关的自由能路径、相稳定性、热力学量的不确定性，以及势函数误差如何传递到宏观性质。

### 9. Scalable long-range machine learning interatomic potentials with electrical response for atomistic material modeling

- Source: arXiv
- Date: 2026-10-16T15:44:07Z
- Venue: cond-mat.mtrl-sci, cs.LG
- Authors: Yicheng Chen, Xiaoyun Yu, Hyejeong Song, Xintian Wang, Zihui Li, Zixi Xia
- Link: https://arxiv.org/abs/2610.23643v1
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential

**中文摘要：** 在电场下对材料进行精确的原子模拟需要在长度尺度上进行长程静电和电响应建模，这超出了传统第一原理方法的范围。然而，这些功能仍然难以与机器学习原子间势（MLIP）的可扩展性相协调。严格的局部模型可以实现高效的空间并行化，但忽略了远程交互，而现有的静电扩展引入了阻碍分布式计算的全局依赖性。 在这里，我们通过分析将长程静电力和玻恩有效电荷（BEC）分离为全局静电计算和学习潜电荷的严格局部导数来克服这一限制。该公式保留了等变 MLIP 的空间可分解性，同时能够跨不同边界条件对能量、力、应力和 BEC 进行分布式评估。 该框架在 \texttt{nvalchemi} 平台上以 DPA4C-LR 的形式实现，可在四个 GPU 上扩展到 520 万个原子，其计算成本约为其短程主干的两倍。经过能量和力的训练，DPA4C-LR 可以准确推断 BEC 并再现水的场相关红外光谱。 我们通过恢复弛豫器 \ce{Pb(Mg_{1/3}Nb_{2/3})O3} 特有的微小极化滞后来进一步证明其功能，该滞后在较小的模拟中被有限尺寸效应所掩盖；预测非晶态 \ce{Li_{0.9}NbO_{0.9}Cl_{4.1}} 中室温场驱动离子电导率为 $6.8 \pm 0.7$~mS/cm；并利用平板校正静电对跨硅/金刚石界面的界面热传输进行建模。
**讨论重点：** 严格的局部模型可以实现高效的空间并行化，但忽略了远程交互，而现有的静电扩展引入了阻碍分布式计算的全局依赖性。该框架在 \texttt{nvalchemi} 平台上以 DPA4C-LR 的形式实现，可在四个 GPU 上扩展到 520 万个原子，其计算成本约为其短程主干的两倍。 结合关键词看，阅读时应重点关注机器学习原子间势相关的第一性原理设置、对称性分析、能带或响应函数计算，以及这些量与可观测物性的对应关系。

### 10. From Algebraic Completeness to Orbit Separation: Recursive Separating Invariants for Global Neural Network Potential Energy Surfaces

- Source: arXiv
- Date: 2026-10-15T11:20:02Z
- Venue: physics.chem-ph
- Authors: Yiping Hao, Jing Lou, Bina Fu, Dong H. Zhang
- Link: https://arxiv.org/abs/2610.21700v1
- Score: 8.0
- Match: 标题匹配 neural network potential

**中文摘要：** 置换不变多项式 (PIP) 为全局势能面 (PES) 提供了系统可改进的、保持对称性的表示，但其作为神经网络描述符的高计算成本限制了其在大型分子系统中的应用。基本不变量 (FI) 形成代数完备的生成集，大大减少了描述符的数量，并使神经网络 PES 能够用于更大的系统。然而，随着分子尺寸和复杂性的增加，PES 评估的计算成本仍然很高。 在这里，我们引入了递归分离不变量（RSI），将描述符设计原则从代数完备性转变为轨道分离。 RSI 是通过相关顺序和递归深度系统构建的，提供了计算效率更高的表示。反应性和非反应性系统的基准测试表明，基于 RSI 的神经网络 (RSI-NN) PES 的评估速度比 FI-NN 同类产品快大约一个数量级，并且系统相关的预测精度在多种情况下相当。 这些结果确立了轨道分离作为为全局神经网络 PES 开发有效的对称性保持描述符的有前途的原理。
**讨论重点：** 在这里，我们引入了递归分离不变量（RSI），将描述符设计原则从代数完备性转变为轨道分离。基本不变量 (FI) 形成代数完备的生成集，大大减少了描述符的数量，并使神经网络 PES 能够用于更大的系统。 结合关键词看，阅读时应重点关注神经网络势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

## 凝聚态物理强关联体系和多铁性质

### 1. Majorana corner modes and tunable braiding in an altermagnet-superconductor heterostructure

- Source: arXiv
- Date: 2026-11-05T08:28:17Z
- Venue: cond-mat.supr-con, quant-ph
- Authors: Yingli Gao, Kai Zhang, Ling-Zheng Meng, Junpeng Hou, Ning Li, Ya-Jie Wu
- Link: https://arxiv.org/abs/2611.07645v1
- Score: 24.0
- Match: 摘要匹配 altermagnetism; 摘要匹配 altermagnetic; 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 通常需要塞曼场来实现和操纵马约拉纳角模式，但代价是抑制超导配对。交变磁学为在零净外部磁场下实现马约拉纳角模式提供了一条新途径。在这里，我们提出了一种在蜂窝晶格交替磁体-超导体异质结构中承载马约拉纳角模式的理论方案。与之前对方形晶格的研究相反，交变磁力在蜂窝晶格的各种不等价边缘上产生明显的有效低能边缘质量。 在低能量边缘理论框架内，我们建立了胡须边缘和锯齿形边缘终端出现马约拉纳角模式的条件。我们通过调整异质结构的交变磁各向异性和化学势进一步明确构建了一套完整的克利福德门。我们的结果为马约拉纳角模式的实现和操纵提供了一个有前景的平台。
**讨论重点：** 在这里，我们提出了一种在蜂窝晶格交替磁体-超导体异质结构中承载马约拉纳角模式的理论方案。在低能量边缘理论框架内，我们建立了胡须边缘和锯齿形边缘终端出现马约拉纳角模式的条件。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 2. Non-Perturbative Resolution of Luttinger's Theorem Violations in Strongly Correlated Systems

- Source: arXiv
- Date: 2026-11-05T12:37:27Z
- Venue: cond-mat.str-el
- Authors: Nazzareno Africani, Herbert Eßl, Alessandro Toschi, Michele Fabrizio
- Link: https://arxiv.org/abs/2611.07933v1
- Score: 18.0
- Match: 标题匹配 strongly correlated systems; 最近 3 天发布

**中文摘要：** 多体物理学面临着一个明显的悖论，即在强相关系统中违反鲁廷格定理。该定理将电子数与路廷格计数（虚数格林函数 $G(iε)$ 的对数单调）联系起来，并且在有限磁场下，通过 Streda 公式将霍尔电导率与路廷格计数的磁场导数联系起来。在这里，我们为这个悖论提供了一个非扰动的解决方案。 我们证明了所报告的对卢廷格定理的违反不需要对物理量的骨架图表示进行分解，从而解决了多体理论中长期存在的争论点。此外，我们表明，解释粒子数和路廷格计数之间不匹配的路廷格积分本身就是一个真正的拓扑不变量，直接与路廷格-沃德函数$Φ[G]$相关，而不是单独与格林函数相关。 我们证明这个不变量，就像 $\ln G(iε)$ 本身的单调一样，完全源于松原轨迹的零频率不连续性。
**讨论重点：** 多体物理学面临着一个明显的悖论，即在强相关系统中违反鲁廷格定理。该定理将电子数与路廷格计数（虚数格林函数 $G(iε)$ 的对数单调）联系起来，并且在有限磁场下，通过 Streda 公式将霍尔电导率与路廷格计数的磁场导数联系起来。 结合关键词看，阅读时应重点关注强关联体系相关的有效模型参数、电子关联强度、相图边界以及可与实验对照的谱学或输运信号。

### 3. Continuum Photonic Axion Insulators

- Source: arXiv
- Date: 2026-11-05T12:13:05Z
- Venue: physics.optics, cond-mat.mes-hall, cond-mat.mtrl-sci
- Authors: Mario G. Silveirinha
- Link: https://arxiv.org/abs/2611.07893v1
- Score: 17.0
- Match: 摘要匹配 magnetoelectric coupling; 摘要匹配 altermagnet; 最近 3 天发布

**中文摘要：** 在这里，我研究了在没有晶格的情况下在均匀反演对称电磁连续体中实现轴子拓扑的条件。我引入了一个连续统反演不变量，仅用零波矢和无限波矢极限下材料响应的光谱特性来表示。令人惊讶的是，我们发现标准回旋型材料响应受到强烈约束，并且在相当一般的条件下，不能在一阶微扰理论中打开轴子间隙。 基于晶体光子轴子绝缘体的有效响应与中心对称交替磁体的光学响应之间的类比，识别出一类可以打开轴子间隙的空间色散奇磁电耦合。这些发现表明电磁连续体中不可逆机制的一个有趣的层次结构：均匀回旋性与陈相相关，而奇磁电耦合与轴子相相关。
**讨论重点：** 我引入了一个连续统反演不变量，仅用零波矢和无限波矢极限下材料响应的光谱特性来表示。在这里，我研究了在没有晶格的情况下在均匀反演对称电磁连续体中实现轴子拓扑的条件。 结合关键词看，阅读时应重点关注磁电耦合、交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 4. Single-shot ground-state preparation via strongly coupled baths

- Source: arXiv
- Date: 2026-11-04T19:00:05Z
- Venue: quant-ph, cond-mat.str-el
- Authors: Liang-Hong Mo, Jerome Lloyd, Yuxuan Zhang, Dmitry A. Abanin, Biao Lian
- Link: https://arxiv.org/abs/2611.07021v1
- Score: 16.0
- Match: 摘要匹配 Hubbard model; 摘要匹配 quantum many-body; 最近 3 天发布

**中文摘要：** 准备量子多体系统的基态和热态是量子模拟的核心任务。耗散协议已成为近期和容错硬件的一种有前途的解决方案，但大多数结构依赖于弱系统浴耦合，导致冷却缓慢。在这里，我们在强系统-浴耦合下构建冷却协议，并在单个冷却循环内演示准确的状态准备。 我们的协议将动态倾斜的辅助能量水平与时间相关的耦合相结合，以优化冷却误差和物理时间之间的权衡。对于一般类型的自由费米子系统，我们将动力学精确地简化为两级散射问题：基态冷却成为最大化谐振激发传递同时抑制非绝热加热的控制问题。 然后，我们构建了一系列“Möbius-Ingham”协议，该协议作为循环周期的函数，实现了无间隙光谱的最佳误差缩放和有间隙光谱的主要加热误差的近指数抑制。在我们的自由费米子基准测试中，莫比乌斯-英厄姆冷却位于测试控制中稳态误差和冷却时间之间的帕累托边界。我们进一步证明了它在 Ising 和 $t$-$V$ 链以及二维费米-哈伯德模型相互作用方面的有效性。 最后，我们将我们的构建扩展到吉布斯态制备，展示了如何在单个循环中制备自由费米子热态。
**讨论重点：** 在这里，我们在强系统-浴耦合下构建冷却协议，并在单个冷却循环内演示准确的状态准备。我们进一步证明了它在 Ising 和 $t$-$V$ 链以及二维费米-哈伯德模型相互作用方面的有效性。 结合关键词看，阅读时应重点关注Hubbard 模型、量子多体相关的有效模型参数、电子关联强度、相图边界以及可与实验对照的谱学或输运信号。

### 5. Variational Monte Carlo Study of Superconductivity in a Correlated System with Broken Inversion Symmetry

- Source: arXiv
- Date: 2026-11-04T05:00:56Z
- Venue: cond-mat.supr-con
- Authors: Tsuyoshi Imazu, Katsunori Kubo
- Link: https://arxiv.org/abs/2611.05964v1
- Score: 16.0
- Match: 摘要匹配 Hubbard model; 摘要匹配 unconventional superconductivity; 最近 3 天发布

**中文摘要：** 反演对称性破缺系统中的非常规超导引起了人们极大的兴趣，因为反对称自旋轨道耦合（ASOC）可以强烈影响自旋结构和超导态的稳定性。在本研究中，我们使用变分蒙特卡罗方法研究具有蜂窝网络对称性的相关系统中的超导性。我们考虑单带哈伯德模型，包括现场库仑相互作用 $U$ 和耦合强度 $λ$ 的 ASOC，并比较具有不同配对对称性的几种配对状态。 试验波函数是根据粒子数和 Gutzwiller 投影的 BCS 状态构建的。为了检查每个配对状态的能量稳定性，我们计算变分能量作为间隙幅度的函数，同时优化每个间隙幅度的变分参数 $μ$ 和 Gutzwiller 参数 $g$。在 $U/t = 10$ 时，$f$ 波态在 $λ/t = 0$ 时具有最低的变分能量，而手性 $p$ 波态在 $λ/t = 0.1$ 时变得最有利。 这些结果表明，在存在强电子相关性的情况下，ASOC 强烈影响超导配对态之间的竞争。
**讨论重点：** 在本研究中，我们使用变分蒙特卡罗方法研究具有蜂窝网络对称性的相关系统中的超导性。我们考虑单带哈伯德模型，包括现场库仑相互作用 $U$ 和耦合强度 $λ$ 的 ASOC，并比较具有不同配对对称性的几种配对状态。 结合关键词看，阅读时应重点关注Hubbard 模型、非常规超导相关的有效模型参数、电子关联强度、相图边界以及可与实验对照的谱学或输运信号。

### 6. Interplay between Spin Stripes and Pairing Crossover in the Bilayer Hubbard Model

- Source: arXiv
- Date: 2026-11-04T02:27:52Z
- Venue: cond-mat.str-el
- Authors: Zixuan Jia, Xuelei Sui, Shijie Hu, Tianxing Ma, Haiqing Lin, Bing Huang
- Link: https://arxiv.org/abs/2611.05840v1
- Score: 16.0
- Match: 标题匹配 Hubbard model; 最近 3 天发布

**中文摘要：** 双层镍酸盐 \ce{La3Ni2O7} 中是否存在 $d$ 波或 $s_\pm$ 波配对尚未解决，并且其观察到的自旋顺序和磁激发与配对机制之间的关系尚不清楚。在这里，我们使用最小双层哈伯德模型的有限温度行列式量子蒙特卡罗模拟来研究强层间耦合下的配对竞争，其中层内和层间反铁磁相关性具有相当的强度。 我们发现，随着空穴掺杂的增加，自旋条纹会自发形成，并伴随着主要配对对称性从 $d$ 波到 $s_\pm$ 波的交叉。交叉跟踪自旋相关性相对强度的变化，层间相关性在幅度上超过了层内相关性。与此同时，动态自旋结构因子表现出磁激发的动量依赖性重组，与波动的自旋条纹一致。 我们的结果将自旋波动的结构确定为自旋条纹和配对竞争之间的关键联系，为理解 \ce{La3Ni2O7} 提供了最小模型的视角。
**讨论重点：** 我们发现，随着空穴掺杂的增加，自旋条纹会自发形成，并伴随着主要配对对称性从 $d$ 波到 $s_\pm$ 波的交叉。在这里，我们使用最小双层哈伯德模型的有限温度行列式量子蒙特卡罗模拟来研究强层间耦合下的配对竞争，其中层内和层间反铁磁相关性具有相当的强度。 结合关键词看，阅读时应重点关注Hubbard 模型相关的有效模型参数、电子关联强度、相图边界以及可与实验对照的谱学或输运信号。

### 7. Ferroelectricity and Peierls transition in MOI$_2$ (M=Ta, Nb): a first-principle analysis

- Source: arXiv
- Date: 2026-11-04T02:24:50Z
- Venue: cond-mat.mtrl-sci
- Authors: Carmel Dansou, Charles Paillard, Laurent Bellaiche
- Link: https://arxiv.org/abs/2611.05836v1
- Score: 16.0
- Match: 标题匹配 ferroelectricity; 最近 3 天发布

**中文摘要：** 范德华铁电 NbOI$_2$ 具有极性畸变，这通常归因于其 Nb 链的 Peierls 二聚化。在这里，我们使用第一原理计算和朗道型能量表明，极性不稳定性实际上是一个独特的有序参数，它并非源于 Peierls 模式凝聚，并且三个主要的不同模式在整个 MOI$_2$ 系列中很重要。 它们是极性模式 $P$、反极性模式 $η$ 和 Peierls 模式 $δ$，其稳定性和耦合很大程度上取决于 $M$ 金属元素的性质，同构 TaOI$_2$ 系统在具有 Peirls 畸变的同时不是极性的，这一事实证明了这一点。
**讨论重点：** 范德华铁电 NbOI$_2$ 具有极性畸变，这通常归因于其 Nb 链的 Peierls 二聚化。在这里，我们使用第一原理计算和朗道型能量表明，极性不稳定性实际上是一个独特的有序参数，它并非源于 Peierls 模式凝聚，并且三个主要的不同模式在整个 MOI$_2$ 系列中很重要。 结合关键词看，阅读时应重点关注铁电性相关的极化翻转、磁电耦合、自旋-晶格耦合以及多铁序参量之间的相互制约。

### 8. Dualities in one-dimensional quantum lattice models: Lie groups, Schur-Weyl duality and symmetry breaking

- Source: arXiv
- Date: 2026-11-05T16:55:32Z
- Venue: quant-ph, cond-mat.str-el, math-ph
- Authors: Dante Bosgoed, Frank Verstraete, Laurens Lootens
- Link: https://arxiv.org/abs/2611.08293v1
- Score: 14.0
- Match: 摘要匹配 tensor network; 最近 3 天发布

**中文摘要：** 我们提出了一个用于测量连续对称性的系统框架，并表明 Schur-Weyl 对偶性作为这种具有开放边界条件的构造的实现而自然出现。限制于紧致李群对称性，我们为表现出这些对称性的一维量子晶格模型构建了对偶模型。我们证明矩阵乘积算子能够显式构造对偶理论及其（不可逆）对称性之间的交织体。 在封闭边界条件下，我们可以通过考虑所有可能的扭曲边界条件来关联这些对偶理论的全谱。我们说明了当对偶性作用于 $G$ 对称模型的边界希尔伯特空间时，Peter-Weyl 变换是如何出现的。所提出的框架概括了先前关于单一融合类别对称模型的对偶性的工作。它举例说明了有限对称性和连续对称性的对偶性如何依赖于键代数和晶格中作为双中心化子的对称性表示之间的关系。 我们认为对偶不可逆自发对称性破缺是对称张量网络算法的基础机制。我们说明了 $U(1)$- 和 $SU(2)$-对称量子晶格模型的这些结果。
**讨论重点：** 我们提出了一个用于测量连续对称性的系统框架，并表明 Schur-Weyl 对偶性作为这种具有开放边界条件的构造的实现而自然出现。限制于紧致李群对称性，我们为表现出这些对称性的一维量子晶格模型构建了对偶模型。 结合关键词看，阅读时应重点关注张量网络相关的新方法的假设、训练或计算流程、适用体系，以及与已有方法相比的优势和局限。

### 9. Microscopic Origin and Josephson Signatures of $d$-Wave Superconductivity in Monolayer FeSe

- Source: arXiv
- Date: 2026-11-05T13:54:03Z
- Venue: cond-mat.supr-con, cond-mat.mtrl-sci, cond-mat.str-el
- Authors: Jiong Mei, Lili Wang, Yu-Jie Sun, Kun Jiang
- Link: https://arxiv.org/abs/2611.08037v1
- Score: 14.0
- Match: 摘要匹配 high-temperature superconductivity; 最近 3 天发布

**中文摘要：** SrTiO$_3$ 上的单层 FeSe 表现出具有纯电子费米表面的高温超导性，引发了有关其非常规配对机制的基本问题。受最近约瑟夫森扫描隧道显微镜无节点 $d$ 波超导证据的启发，我们使用实验约束的多轨道理论研究了 Fe $d_{xy}$ 轨道的微观作用。 适合准粒子干涉和角分辨光电子能谱的紧束缚模型揭示了费米能级附近的大量 $d_{xy}$ 特征和主要的最近邻跳跃，与铁基超导体的传统动力学挫败图相反。巡回自旋涨落计算和强耦合交换方法都有利于鲁棒的 $d$ 波配对态，其带间配对分量允许完全间隙的准粒子谱。 我们进一步建立了基于对称性的空间约瑟夫森隧道选择规则，揭示了特征键中心最大值和镜像强制干涉零点，区分了 $d$ 波配对和竞争的 $s$ 波状态。这些对称性增强的节点线在 Fe 位点杂质附近存在，而尽管失去了镜面保护，$d$ 波和 $s$ 波约瑟夫森模式之间的明显对比仍然存在于涡旋周围。 我们的结果将非常规的 $d_{xy}$ 电子结构与无节点 $d$ 波超导性联系起来，并证明了空间约瑟夫森干涉在解决多轨道超导体中的配对对称性方面的力量。
**讨论重点：** 受最近约瑟夫森扫描隧道显微镜无节点 $d$ 波超导证据的启发，我们使用实验约束的多轨道理论研究了 Fe $d_{xy}$ 轨道的微观作用。适合准粒子干涉和角分辨光电子能谱的紧束缚模型揭示了费米能级附近的大量 $d_{xy}$ 特征和主要的最近邻跳跃，与铁基超导体的传统动力学挫败图相反。 结合关键词看，阅读时应重点关注高温超导相关的样品制备、实验表征条件、关键观测信号，以及这些信号如何支撑物理机制解释。

### 10. Observable-Based Learning of Effective Entanglement Hamiltonians

- Source: arXiv
- Date: 2026-11-05T02:43:38Z
- Venue: cond-mat.str-el, cond-mat.stat-mech, quant-ph
- Authors: Siyi Yang, Yuzhi Liu, Yi-Ming Ding, Zheng Yan
- Link: https://arxiv.org/abs/2611.07353v1
- Score: 13.0
- Match: 摘要匹配 quantum many-body; 最近 3 天发布

**中文摘要：** 除了特殊的分析易处理情况之外，确定相互作用的量子多体系统的纠缠哈密顿量（EH）仍然是一个基本挑战。在这里，我们开发了一个用于学习有效 EH 的可观察匹配框架，我们使用量子蒙特卡罗的响应估计来演示该框架。 作为该框架的应用，我们首先使用等时间相关性校准晶格 Bisognano-Wichmann (LBW) 结构的整体前因子，然后学习超出其规定轮廓的空间解析耦合，而不假设其空间依赖性的特定函数形式。仅根据局部相关性进行训练，学习到的 EH 在 $1$D 中重现基准冯诺依曼和第二 Rényi 熵，在 $2$D 中重现第二 Rényi 熵。 对于与 $(2+1)$D $O(3)$ Wilson-Fisher 临界点处的特殊表面临界性相关的强键切割，自由形式学习在预测第二个 Rényi 熵方面优于校准的 LBW ansatz，并揭示了空间非均匀耦合重正化。重要的是，学习到的 EH 还提供了在这种情况下访问冯·诺依曼熵的方法，揭示了负的次领先修正并将之前的 Rényi 熵发现扩展到冯·诺依曼的情况。 对于传统的数值方法来说，直接评估这种 $(2+1)$D 相互作用的量子多体系统中的冯诺依曼熵仍然具有挑战性。这些结果建立了基于可观察的学习作为在高维交互系统中构建超出规定空间轮廓的有效纠缠哈密顿量的途径。
**讨论重点：** 在这里，我们开发了一个用于学习有效 EH 的可观察匹配框架，我们使用量子蒙特卡罗的响应估计来演示该框架。作为该框架的应用，我们首先使用等时间相关性校准晶格 Bisognano-Wichmann (LBW) 结构的整体前因子，然后学习超出其规定轮廓的空间解析耦合，而不假设其空间依赖性的特定函数形式。 结合关键词看，阅读时应重点关注量子多体相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。
