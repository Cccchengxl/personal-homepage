# Latest papers for 程旭丽

Updated: 2026-11-25T06:40:46.524780+00:00
Window: last 14 days

## Notes

- arXiv query failed for 机器学习分子动力学模拟与热力学性质: The read operation timed out
- 机器学习分子动力学模拟与热力学性质 kept previous papers because the current query returned 0 results.
- arXiv query failed for 凝聚态物理强关联体系和多铁性质: HTTP Error 429: Unknown Error
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

**中文摘要：** 机器学习原子间势能在大长度和时间尺度上以接近 \textit{ab initio} 的精度实现原子模拟。基础模型将这种能力扩展到整个元素周期表，但继承了用于生成训练数据的电子结构方法的热力学描述。因此，相对相位稳定性的小误差可能会导致转变温度的大误差。 我们引入了附加热力学校正层，该层可将相自由能移向评估参考，而无需重新训练或修改基础电势。一阶热力学结构将所需的相自由能位移直接转换为构型能量目标，该目标使用线性原子团簇展开进行拟合，并根据测量的自由能迭代细化。我们使用基础 GRACE 模型将该方法应用于具有不同晶体结构的元素之间的熔化和固体到固体的转变。 校正后，所有转变温度均位于评估值的规定公差范围内，包括 Ca、Ti 和 Zr，其中固相转变和熔化一起校正。静态能量曲线、体积模量和液体结构仍然接近基础模型。空位形成能、热膨胀和液体密度取决于校正后的相平衡以及校正较大时的变化。该方法既不需要重新训练、可微分动力学，也不需要访问基础势的参数。 它提供了一种将可转移原子模型与评估相热力学相结合的模块化途径。
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

### 1. Magnetization-free quantum anomalous Hall effect in altermagnetic weak topological insulators

- Source: arXiv
- Date: 2026-11-10T03:22:11Z
- Venue: cond-mat.mes-hall
- Authors: Yanmiao Han, Yu-Hao Wan, Peng-Yi Liu, Rundong Zhao, Qing-Feng Sun
- Link: https://arxiv.org/abs/2611.13508v1
- Score: 27.0
- Match: 摘要匹配 ferromagnetism; 标题匹配 altermagnetic; 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 量子反常霍尔（QAH）效应通常通过铁磁性或磁性掺杂来实现，这限制了材料的选择，并且常常导致低迁移率、无序敏感性和低工作温度。在这里，我们提出了一种在弱拓扑绝缘体（WTI）上使用交变磁交换来实现无净磁化的 QAH 相的机制。 交变磁序选择性地在 Z 点处使狄拉克锥产生间隙，而 WTI 薄膜的顶面和底面之间的杂化在该点处打开了一个微不足道的间隙，从而生成具有单个手性边缘通道的陈数 C = 1 相。我们通过最小薄膜模型和平板几何形状验证拓扑转变，并计算相关的霍尔响应。由于交替磁体和层状 WTI 已经在实验中存在，因此该机制提供了一种有前景且可通过实验实现的途径，无需磁掺杂或全局磁化即可实现 QAH 相。 结果表明，交变磁表面工程可以为实现层状量子材料中的无耗散边缘传输提供干净且可控的途径。
**讨论重点：** 在这里，我们提出了一种在弱拓扑绝缘体（WTI）上使用交变磁交换来实现无净磁化的 QAH 相的机制。我们通过最小薄膜模型和平板几何形状验证拓扑转变，并计算相关的霍尔响应。 结合关键词看，阅读时应重点关注铁磁性、交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 2. Geometry-Selective Higher-order topological insulators induced by $d_{xy}$ altermagnet

- Source: arXiv
- Date: 2026-11-10T01:26:22Z
- Venue: cond-mat.mes-hall
- Authors: Siyuan Cheng, Yuee Xie, Xiaosen Yang, Yuanping Chen
- Link: https://arxiv.org/abs/2611.13438v1
- Score: 23.0
- Match: 摘要匹配 altermagnetism; 摘要匹配 altermagnetic; 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 我们表明，接近 $d_{xy}$ 波交变磁体为工程边界几何相关的高阶拓扑相提供了有效的途径。边界几何形状在确定拓扑特性中起着至关重要的作用：轴对齐的边缘状态保持无间隙，而对角边缘获得具有交替符号的有效质量，从而产生位于质量域壁处的四个角模式。通过投影到边缘状态子空间，我们得出不同边界几何形状的有效边缘哈密顿量。 此外，在周期性边界条件下引入的$π$-磁通缺陷产生位于磁通核心处的零能量束缚态，为没有物理边界的非平凡拓扑提供了补充证据。塞曼场和交变磁序之间的相互作用通过边缘间隙的关闭和重新打开驱动拓扑转变，而体间隙保持打开。 这些发现强调了边界几何在高阶拓扑中的关键作用，并建立了邻近感应 $d_{xy}$ 波交变磁性作为设计高阶拓扑相的途径。
**讨论重点：** 我们表明，接近 $d_{xy}$ 波交变磁体为工程边界几何相关的高阶拓扑相提供了有效的途径。边界几何形状在确定拓扑特性中起着至关重要的作用：轴对齐的边缘状态保持无间隙，而对角边缘获得具有交替符号的有效质量，从而产生位于质量域壁处的四个角模式。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 3. Particle-hole asymmetry and a fluctuating pair-density-wave state in a lightly doped Mott insulator on the square lattice

- Source: arXiv
- Date: 2026-11-10T13:56:16Z
- Venue: cond-mat.str-el, cond-mat.supr-con, physics.comp-ph
- Authors: Hao-Xin Wang, Zheng-Yuan Yue, Wen-Yuan Liu, Zheng-Cheng Gu
- Link: https://arxiv.org/abs/2611.14101v1
- Score: 18.0
- Match: 标题匹配 Mott insulator; 最近 3 天发布

**中文摘要：** 方形晶格上的轻掺杂莫特绝缘体是否支持强大的 $d$ 波超导仍然是强相关物理学和铜酸盐超导微观理论中的中心问题。实验和数值研究揭示了明显的粒子空穴不对称性，表明 $d$ 波超导性、对密度波 (PDW)、条纹、电荷密​​度波 (CDW) 和反铁磁相关性之间存在微妙的竞争。 在这里，我们结合大规模 DMRG 和有限尺寸 PEPS 来研究低掺杂 $δ\leq 0.1$ 下的方晶格 $t$-$J$ 模型，同时将近邻跳跃 $t'$ 从类电子 ($t'>0$) 调整为类空穴 ($t'<0$) 状态。类似电子的一侧支持强大的、几乎均匀的$d$波配对，而减少$t'$会引起二周期斑块调制，并最终在类空穴一侧产生电荷主导的状态，其静态配对幅度受到强烈抑制。 对开放地带和正方形的 DMRG 计算，以及对高达 16\times16$ 站点的开放正方形的 PEPS 计算，支持了这种演变。在具有 $C_4$ 对称哈密顿量的正方形上，两种方法都发现类空穴态的配对相关性选择斑动量 $(π,0)$ 和 $(0,π)$ 并在几个晶格间距内衰减，而占主导地位的电荷密度调制形成双向棋盘，其周期外推至约 $4a_0$，接近于轻掺杂 Bi-2201 中观察到的情况。 这些观察结果在轻掺杂类空穴区域中建立了波动的斑块 PDW，其中局部对携带有限的动量但缺乏相位相干性。我们的结果牢固地确立了粒子空穴不对称性作为轻掺杂 $t$-$J$ 模型中竞争配对趋势的中心组织原则。
**讨论重点：** 在这里，我们结合大规模 DMRG 和有限尺寸 PEPS 来研究低掺杂 $δ\leq 0.1$ 下的方晶格 $t$-$J$ 模型，同时将近邻跳跃 $t'$ 从类电子 ($t'>0$) 调整为类空穴 ($t'<0$) 状态。实验和数值研究揭示了明显的粒子空穴不对称性，表明 $d$ 波超导性、对密度波 (PDW)、条纹、电荷密​​度波 (CDW) 和反铁磁相关性之间存在微妙的竞争。 结合关键词看，阅读时应重点关注Mott 绝缘体相关的有效模型参数、电子关联强度、相图边界以及可与实验对照的谱学或输运信号。

### 4. Emergent Quantized Zak Phases without Dimerization in a Multicomponent Fermionic Extended Hubbard Model

- Source: arXiv
- Date: 2026-11-10T07:42:19Z
- Venue: cond-mat.str-el
- Authors: F. X. Liu, Z. Song
- Link: https://arxiv.org/abs/2611.13695v1
- Score: 18.0
- Match: 标题匹配 Hubbard model; 最近 3 天发布

**中文摘要：** 量子化 Zak 相通常与二聚系统相关，例如非相互作用的 Su--Schrieffer--Heeger (SSH) 模型。然而，在相互作用的系统中，即使在底层晶格中不存在显式二聚化的情况下，相互作用也可以诱导粒子簇的有效二聚化。在这项工作中，我们研究了现场相互作用和最近邻相互作用之间共振条件下的一维多分量费米子扩展哈伯德模型。 我们发现奇数费米子数 $n\geqslant 3$ 出现量化的 Zak 相位，受到有效哈密顿量的反演对称性的保护。此外，在存在倾斜场的情况下，费米子簇表现出布洛赫振荡，在此期间，可以从一个布洛赫周期内高斯波包的演化中提取它们的 Zak 相位。我们的结果揭示了一种相互作用诱导机制，可在多组分费米子系统中实现量子化 Zak 相，而无需显式晶格二聚化。
**讨论重点：** 在这项工作中，我们研究了现场相互作用和最近邻相互作用之间共振条件下的一维多分量费米子扩展哈伯德模型。量子化 Zak 相通常与二聚系统相关，例如非相互作用的 Su--Schrieffer--Heeger (SSH) 模型。 结合关键词看，阅读时应重点关注Hubbard 模型相关的有效模型参数、电子关联强度、相图边界以及可与实验对照的谱学或输运信号。

### 5. Probing Chern Topology through Hall-Sensitive Photonic Spin Hall Shifts in a d-wave Altermagnet

- Source: arXiv
- Date: 2026-11-07T12:57:01Z
- Venue: cond-mat.mes-hall
- Authors: Mahnoor Sajid, Maha Siddiqui, Muzamil Shah
- Link: https://arxiv.org/abs/2611.10706v1
- Score: 18.0
- Match: 摘要匹配 altermagnetic; 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 在本文中，我们研究了二维 Rashba 耦合 $d$ 波交变磁陈系统中的光子自旋霍尔效应，该系统受到均匀的面外交换场的影响。我们首先分析高对称点处的能带结构和狄拉克质量分布，其中$m_Γ=m_M=Δ_x，m_X=Δ_x-4 t_J$，$m_Y=Δ_x+4 t_J$。高对称点处的能带反转会产生拓扑平凡状态 $(C=0)$ 和陈绝缘相 $(C= \pm 1)$。 采用 Kubo 形式来计算光导率，并结合基底支撑的导电片的反射矩阵，我们计算反射高斯光束的螺旋性相关的有限腰位移。由此产生的光学响应表现出最小带间吸收阈值、范霍夫型光谱特征以及由于交换场的动量依赖性而在 $X$ 和 $Y$ 点处产生的明显跃迁。 在指定的霍尔张量和偏振符号约定下，纵向螺旋半分离在光学霍尔电导率反转时是奇数，并且相应地在相反的陈相位之间改变符号，而横向半分离在霍尔响应中是偶数。最大的自旋相关分裂发生在伪布鲁斯特反射率最小值附近。 纵向自旋分裂反转了相反的陈相之间的符号，反映了交换控制的光学霍尔响应，而其明显的光谱变化揭示了 $d$ 波交磁交换引起的不等价带间跃迁的影响。这些发现将偏振分辨光子束位移确立为霍尔活性拓扑相及其特征光谱的敏感探针。
**讨论重点：** 在本文中，我们研究了二维 Rashba 耦合 $d$ 波交变磁陈系统中的光子自旋霍尔效应，该系统受到均匀的面外交换场的影响。我们首先分析高对称点处的能带结构和狄拉克质量分布，其中$m_Γ=m_M=Δ_x，m_X=Δ_x-4 t_J$，$m_Y=Δ_x+4 t_J$。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 6. Hidden interfacial magnetism in RuO$_2$ heterostructures revealed by a superconducting spin switch

- Source: arXiv
- Date: 2026-11-10T04:53:04Z
- Venue: cond-mat.mtrl-sci, cond-mat.supr-con
- Authors: Tetsuma Mandokoro, Hisakazu Matsuki, Shutaro Karube, Rodrigo de las Heras, Andrei Mazanik, Akihiro Yamada
- Link: https://arxiv.org/abs/2611.13579v1
- Score: 17.0
- Match: 摘要匹配 altermagnetic; 摘要匹配 altermagnet; 最近 3 天发布

**中文摘要：** RuO$_2$，曾经是旗舰的变磁候选者，现在被认为在整体上是非磁性的，但在其表面和界面处出现了微弱的、静态的和空间不均匀的磁性。这种磁力驻留在哪里，是什么稳定了它，以及它是否与这些状态有关仍然是悬而未决的问题。在这里，我们使用超导自旋开关在 Nb/RuO$_2$ 界面上解决这些问题。 GdN/Nb/RuO$_2$ 三层允许界面交换场排列来调节 Nb 的超导转变温度，探测传统磁力测量无法达到的界面磁性。该开关揭示了一个隐藏的磁性子系统，我们将其归因于 Nb 从 RuO$_2$ 中清除氧气时形成的薄 RuO$_x$ 氧化还原层。 This layer behaves as a weak and magnetically hard ferromagnet with vacancy-induced anisotropy.此外，超电流放大了开关效率，使探头灵敏度可原位可调。 因此，超导自旋开关成为埋藏界面隐藏磁性的定量低温探针。
**讨论重点：** RuO$_2$，曾经是旗舰的变磁候选者，现在被认为在整体上是非磁性的，但在其表面和界面处出现了微弱的、静态的和空间不均匀的磁性。这种磁力驻留在哪里，是什么稳定了它，以及它是否与这些状态有关仍然是悬而未决的问题。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 7. Hybridization-brightened interlayer excitons in multilayer WSe2 controlled by sliding ferroelectricity

- Source: arXiv
- Date: 2026-11-09T21:32:33Z
- Venue: cond-mat.mtrl-sci
- Authors: Youngki Yeo, Idan Kizel, Dror Hershkovitz, Omri Meron, Iva Plutnarova, Zdenek Sofer
- Link: https://arxiv.org/abs/2611.13264v1
- Score: 17.0
- Match: 标题匹配 ferroelectricity; 最近 3 天发布

**中文摘要：** 层间激子（IX）将空间分离的电子和空穴波函数与电可调偶极矩结合在一起，但它们减少的波函数重叠通常会限制光发射，特别是对于高能态。在这里，我们报告了少层 WSe2 中接近 2.23 eV 的明亮、光谱窄的高能层间激子 (h-IX)，并研究了其光学活性如何随层数和滑动铁电极化而演变。在原始的 2H-WSe2 中，我们观察到高能激子发射的厚度依赖性增亮。 GW-BSE 计算揭示了混合的层内和层间结构，具有增强的光学重量，表明多层杂化有助于观察到的增亮。在包含滑动铁电界面的平行堆叠 3L/3L WSe2 中，h-IX 表现出偏振相关能量和区分 Pup 和 Pdown 域的 Stark 响应。电场驱动的畴壁运动在两个 h-IX 分支之间产生光谱权重的滞后转移，从而实现铁电开关的光学跟踪。 这些结果将多层杂化确立为光学活性高能层间激子的途径，并将滑动铁电性作为控制其能量、偶极子和发射的互补自由度。
**讨论重点：** 在这里，我们报告了少层 WSe2 中接近 2.23 eV 的明亮、光谱窄的高能层间激子 (h-IX)，并研究了其光学活性如何随层数和滑动铁电极化而演变。在原始的 2H-WSe2 中，我们观察到高能激子发射的厚度依赖性增亮。 结合关键词看，阅读时应重点关注铁电性相关的极化翻转、磁电耦合、自旋-晶格耦合以及多铁序参量之间的相互制约。

### 8. Chiral Superconductivity Indifferent to Parent Topology in the Square-Lattice Hofstadter-Hubbard Model

- Source: arXiv
- Date: 2026-11-09T19:00:02Z
- Venue: cond-mat.str-el, cond-mat.supr-con
- Authors: Jia-Xin Zhang, Wen O. Wang, Leon Balents, Lucile Savary, D. N. Sheng
- Link: https://arxiv.org/abs/2611.13091v1
- Score: 17.0
- Match: 标题匹配 Hubbard model; 最近 3 天发布

**中文摘要：** 我们研究了 $π$-通量方格 $t$-$t'$ Hofstadter-Hubbard 模型，该模型建议在扭曲莫尔双层中实现。 通过在半填充时调整 $U$ 和 $t'$，基态密度矩阵重整化群模拟 (DMRG) 和部分子分析识别出相图中的整数量子霍尔 (IQH) 相、手性自旋液体 (CSL) 和反铁磁体 (AFM)，而有限温度行列式量子蒙特卡罗 (DQMC) 的电荷和自旋涨落表明电荷能隙闭合，但 IQH-CSL 边界处存在开放的自旋能隙，与那里预期的拓扑临界性。 因此，该模型会生成一个相图，其中并排包含弱相关能带拓扑 (IQH)、本征拓扑序 (CSL) 和传统对称破缺 (AFM)。在掺杂这三个母相中的任何一个后，具有自旋陈数 $C_s=-2$ 的单个手性拓扑超导体几乎占据了整个相图。 DMRG、DQMC 和弱耦合微扰理论都同意其配对对称性。 这表明，无论底层相关半填充态的特征及其磁波动如何，无论是 IQH、自旋液体还是弱波动 AFM，掺杂我们模型的拓扑带都会在整个相图中稳健地诱导相同的配对态。
**讨论重点：** 我们研究了 $π$-通量方格 $t$-$t'$ Hofstadter-Hubbard 模型，该模型建议在扭曲莫尔双层中实现。 通过在半填充时调整 $U$ 和 $t'$，基态密度矩阵重整化群模拟 (DMRG) 和部分子分析识别出相图中的整数量子霍尔 (IQH) 相、手性自旋液体 (CSL) 和反铁磁体 (AFM)，而有限温度行列式量子蒙特卡罗 (DQMC) 的电荷和自旋涨落表明电荷能隙闭合，但 IQH-CSL 边界处存在开放的自旋能隙，与那里预期的拓扑临界性。 结合关键词看，阅读时应重点关注Hubbard 模型相关的有效模型参数、电子关联强度、相图边界以及可与实验对照的谱学或输运信号。

### 9. Higher tensor network states in two spatial dimensions: fundamental theorem for open boundary conditions

- Source: arXiv
- Date: 2026-11-09T16:25:50Z
- Venue: cond-mat.str-el, math-ph, quant-ph
- Authors: Clement Delcamp, Boris Kjær
- Link: https://arxiv.org/abs/2611.12658v1
- Score: 17.0
- Match: 标题匹配 tensor network; 最近 3 天发布

**中文摘要：** 我们引入一类通过对矩阵乘积状态进行分类获得的二维张量网络状态。这个过程使我们考虑由与底层晶格的 2 单元相关联的 2 向量空间提供的键空间。然后，张量网络表示被定义为编码晶格几何的幺半群签名上的自由幺半群类别上的模块类别。我们证明了一个基本定理，指出在适当的开放边界条件下生成相同状态的两个表示作为模块类别是等效的。 最后，我们引入 2-注入性的概念，这是矩阵乘积状态的注入性条件的分类模拟。
**讨论重点：** 我们引入一类通过对矩阵乘积状态进行分类获得的二维张量网络状态。这个过程使我们考虑由与底层晶格的 2 单元相关联的 2 向量空间提供的键空间。 结合关键词看，阅读时应重点关注张量网络相关的新方法的假设、训练或计算流程、适用体系，以及与已有方法相比的优势和局限。

### 10. Topological states in fractals through a self-similar tensor network encoding

- Source: arXiv
- Date: 2026-11-09T15:16:40Z
- Venue: cond-mat.mes-hall, quant-ph
- Authors: Zebedeus F. Osseweijer, Jagoda Malag, Jose L. Lado, Tiago V. C. Antão, Anouar Moustaj
- Link: https://arxiv.org/abs/2611.12546v1
- Score: 17.0
- Match: 标题匹配 tensor network; 最近 3 天发布

**中文摘要：** 张量网络方法在解决指数级大型多体问题方面发挥了重要作用。最近，这些技术还应用于单粒子紧束缚哈密顿量，允许在指数大晶格上评估可观测量。在这里，我们证明这些方法的尺度分离性质允许对自相似结构进行自然编码，例如 Sierpiński 垫片，这是一种豪斯多夫维 $\log 3/\log 2 \approx 1.58$ 的尺度不变分形，在此类格子上产生哈密顿量的精确而紧凑的表示。 使用这种编码，我们研究了陈绝缘体，即仅限于这种分形几何的通量戈薇模型，并开发了在张量网络框架内研究其拓扑状态的方法。这使我们能够比稠密矩阵方法获得更高的分形生成，从而解决了具有超过 1 亿个位点的深层分形的状态密度。 此外，较大的结构使我们能够解析较小间隙中的拓扑，这表明这些方法可能有助于理解拓扑和非整数维度之间的相互作用。
**讨论重点：** 使用这种编码，我们研究了陈绝缘体，即仅限于这种分形几何的通量戈薇模型，并开发了在张量网络框架内研究其拓扑状态的方法。最近，这些技术还应用于单粒子紧束缚哈密顿量，允许在指数大晶格上评估可观测量。 结合关键词看，阅读时应重点关注张量网络相关的新方法的假设、训练或计算流程、适用体系，以及与已有方法相比的优势和局限。
