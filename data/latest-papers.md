# Latest papers for 程旭丽

Updated: 2026-08-25T01:00:06.353831+00:00
Window: last 14 days

## Notes

- arXiv query failed for 机器学习分子动力学模拟与热力学性质: HTTP Error 429: Unknown Error
- 机器学习分子动力学模拟与热力学性质 kept previous papers because the current query returned 0 results.
- arXiv query failed for 凝聚态物理强关联体系和多铁性质: HTTP Error 429: Unknown Error
- 凝聚态物理强关联体系和多铁性质 returned 1 papers; target range is 5-10.

## 机器学习分子动力学模拟与热力学性质

### 1. Unlocking Multi-Component Bulk-Materials Molecular Dynamics with a Small-Footprint Machine Learning Interatomic Potential

- Source: arXiv
- Date: 2026-08-17T09:32:51Z
- Venue: physics.comp-ph
- Authors: Yucheng Ouyang, Xin Chen, Ying Liu, Lifang Wang, Xingyu Gao, Xiawei Du
- Link: https://arxiv.org/abs/2608.16329v1
- Score: 13.0
- Match: 标题匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 与纳米材料相反，散装材料需要在大空间尺度（约10 ^ 9个或更多原子）上进行分子动力学（ MD ）模拟，以充分捕捉其原子尺度的物理特性。以前，机器学习原子间势（ MLIP ）的引入已经将MD扩展到这个规模，但即使是单组件批量系统也需要高端超级计算机上的数万个GPU。 QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS
**讨论重点：** 与纳米材料相反，散装材料需要在大空间尺度（约10 ^ 9个或更多原子）上进行分子动力学（ MD ）模拟，以充分捕捉其原子尺度的物理特性。以前，机器学习原子间势（ MLIP ）的引入已经将MD扩展到这个规模，但即使是单组件批量系统也需要高端超级计算机上的数万个GPU。 结合关键词看，阅读时应重点关注机器学习原子间势相关的模拟体系、时间尺度、温度条件、动力学稳定性，以及有限温度性质对势函数质量的敏感性。

### 2. ChemReporter: A Framework for Curating and Exporting Large-Scale Chemical Datasets for MLIP Training

- Source: arXiv
- Date: 2026-08-17T11:15:35Z
- Venue: physics.chem-ph, physics.atom-ph
- Authors: Marie Bluntzer, Jules Tilly, Christoph Brunken
- Link: https://arxiv.org/abs/2608.16418v1
- Score: 9.0
- Match: 摘要匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 训练集的质量和多样性是机器学习原子间势（ MLIP ）可靠性的关键决定因素，但完全使用海量数据集通常是不切实际和多余的，因此智能数据选择至关重要。然而，一个主要瓶颈是缺乏统一访问、策划和子采样异构大规模化学数据集的基础设施，这些数据集在结构、元数据和文件格式方面存在很大差异。 我们通过ChemReporter来解决这一差距， ChemReporter是一个模块化的、与方法无关的框架，可将任意分子和材料数据集转换为统一的可查询表示，并将结果直接导出到MLIP就绪的训练数据中。 ChemReporter分为三个解耦阶段：处理，将原始数据集解析为富含结构、物理和化学元数据的分区Apache Parquet存储库；查询，通过CLI或Python API使用任意选择标准过滤和采样此存储库，从简单的物理约束到自定义、用户定义的策略；导出，将所选子集流式传输到HDF5文件中，以便在现代MLIP培训框架中直接使用。 在整个过程中，每个导出的数据点都可以追溯到其原始源条目，并且可以在相同的配置和查询数据库版本下可靠地再现数据集导出。由于数据以可查询的磁盘备份格式存储，因此ChemReporter可以处理远大于可用内存的数据集，使其能够在标准计算基础设施上扩展到十亿结构的数据集。ChemReporter在GitHub和PyPI上以Apache许可证2.0提供。
**讨论重点：** 我们通过ChemReporter来解决这一差距， ChemReporter是一个模块化的、与方法无关的框架，可将任意分子和材料数据集转换为统一的可查询表示，并将结果直接导出到MLIP就绪的训练数据中。然而，一个主要瓶颈是缺乏统一访问、策划和子采样异构大规模化学数据集的基础设施，这些数据集在结构、元数据和文件格式方面存在很大差异。 结合关键词看，阅读时应重点关注机器学习原子间势相关的新方法的假设、训练或计算流程、适用体系，以及与已有方法相比的优势和局限。

### 3. Cross-Geometry Transferability Assessment of Universal Machine Learning Interatomic Potentials: From Bulk Materials to Atomic Nanowires

- Source: arXiv
- Date: 2026-08-07T00:15:49Z
- Venue: cond-mat.mtrl-sci, cond-mat.mes-hall, physics.comp-ph
- Authors: Pedro H. M. Zanineli, Bruno Focassio, Gabriel R. Schleder
- Link: https://arxiv.org/abs/2608.06662v1
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential

**中文摘要：** QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS
**讨论重点：** 在这里，我们构建了一个ZrO2配置的密度函数理论数据集，该数据集跨越体积、板坯、颗粒、颈部和原子薄线环境，其动机是实验观察到的涉及颈部变薄和原子线形成的ZrO2脱烧过程。我们首先对26个预训练的MLIP进行基准测试，并在零点预测中观察到明显的几何相关性退化。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 4. Ultrafast Nonthermal Lattice Destabilization and Suppression of Polar Optical Scattering in Electronically Excited $α$-SiO$_2$ from First-Principles and Deep Neural Network Potential Modeling

- Source: arXiv
- Date: 2026-07-30T21:04:07Z
- Venue: cond-mat.mtrl-sci, physics.comp-ph
- Authors: Iyyappa Rajan Panneerselvam, Mark Yeung, Charlotte Palmer, Brendan Dromey, Lorenzo Stella
- Link: https://arxiv.org/abs/2607.28838v1
- Score: 8.0
- Match: 标题匹配 neural network potential

**中文摘要：** 我们提出了一种多尺度第一原理到机器学习的方法来研究电子激发$ α $ -SiO $_2 $中的超快晶格动力学。基于电子温度相关密度泛函理论（ DFT ）的从头分子动力学（ AIMD ）用于训练电子温度相关深度神经网络电位（ DNNP ）。使用DNNP可以以接近DFT的精度对具有数千个原子的大型$ α $ -SiO $_2 $电池进行原子学建模。 特别是， DNNPs使我们能够获得电子温度突然升高所激发的$ α $ -SiO $_2 $的准确声子带结构和分子动力学（ MD ）。随着电子温度的升高， $ T_e $发现了$ α $ -SiO $_2 $的明显晶格不稳定性，这可以通过违反弹性稳定性标准、大量体积膨胀、体积模量的急剧降低以及由于反键态占据而导致的Si-O键的逐渐减弱来证明。 QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS 这种行为解释了$ T_e $突然上升后动态温度的非单调平衡。在$ T_e $升至2.6 eV后， Si和O原子首先在两个不同的温度下分别平衡，这表明原子流体相与最近的实验和理论发现一致。
**讨论重点：** 我们提出了一种多尺度第一原理到机器学习的方法来研究电子激发$ α $ -SiO $_2 $中的超快晶格动力学。基于电子温度相关密度泛函理论（ DFT ）的从头分子动力学（ AIMD ）用于训练电子温度相关深度神经网络电位（ DNNP ）。 结合关键词看，阅读时应重点关注神经网络势相关的模拟体系、时间尺度、温度条件、动力学稳定性，以及有限温度性质对势函数质量的敏感性。

### 5. PASS: Perturbation augmented space group structure sampling for transferable Fe-O machine learning interatomic potential

- Source: arXiv
- Date: 2026-07-30T10:48:01Z
- Venue: cond-mat.mtrl-sci, physics.comp-ph
- Authors: Zixiong Wei, Fei Shuang, Poulumi Dey
- Link: https://arxiv.org/abs/2607.28000v1
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential

**中文摘要：** QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS 我们提出了一种基于原子簇扩展（ ACE ）框架为Fe-O系统开发首个此类可转移机器学习原子间势（ MLIP ）的系统方法。我们通过批量、表面和界面特性，彻底验证ACE MLIP在纯Fe和Fe-O系统上的准确性和能力。我们展示了在使用ACE MLIP的大规模Fe氧化模拟中FeO样结构的形成。 这项工作表明， PASS方法产生了准确且可转移的MLIP ，能够捕获氧化物生长的反应复杂性，同时在扩展系统中保持计算实用性。
**讨论重点：** 在这项工作中，我们提出了扰动增强空间群结构采样（ PASS ）方法，以生成由小于10个原子的小细胞结构组成的广泛而有代表性的数据集。然而， Fe-oxygen (O)系统以其结构和磁性复杂性而闻名，这使得生成高质量数据集具有挑战性。 结合关键词看，阅读时应重点关注机器学习原子间势相关的第一性原理设置、对称性分析、能带或响应函数计算，以及这些量与可观测物性的对应关系。

### 6. Extracting Atomic Environments for Machine Learning Interatomic Potentials

- Source: arXiv
- Date: 2026-07-28T17:28:41Z
- Venue: cond-mat.mtrl-sci
- Authors: Jared C. Stimac, Fei Zhou, Kyle Bushick, Bo Lei, Sebastien Hamel, Amit Samanta
- Link: https://arxiv.org/abs/2607.26018v2
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential

**中文摘要：** 为了通过原子模拟（如分子动力学（ MD ） ）适当地捕获大规模材料特征和出现的现象，系统规模可以达到数亿个原子。然而，驱动这些模拟的力场模型通常使用密度泛函理论（ DFT ）参考数据进行训练，仅限于大约100或1000个原子的相对较小的配置。 为了计算感兴趣区域的原子上的DFT力，例如用于主动学习或原子间势的即时训练，需要从较大的模拟框中提取一小组原子，并且通常使用DFT的周期性边界条件。然而，尚未系统地分析选择这一提取原子集合的形状和大小以及生成潜在必要的钝化包络的方法。 QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS
**讨论重点：** QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 7. Charge-Density-Wave Phase Transitions in Monolayer 1T-TaS2 from Universal Machine Learning Molecular Dynamics

- Source: arXiv
- Date: 2026-07-24T13:57:09Z
- Venue: cond-mat.mtrl-sci
- Authors: Valentina Nesterova, Tribhuwan Pandey, Tom Berlijn, Fariborz Kargar, Lucas Lindsay, Konstantin Klyukin
- Link: https://arxiv.org/abs/2607.22316v1
- Score: 8.0
- Match: 标题匹配 machine learning molecular dynamics

**中文摘要：** 1T过渡金属二硫族化物中的电荷密度波（ CDW ）相源于强电子-声子耦合和伴随的晶格不稳定性。由于需要大型超级电池和广泛的有限温度采样，使用传统的第一原理分子动力学（ MD ）捕获它们的温度依赖性结构演变仍然具有挑战性。 在这里，我们结合密度泛函理论（ DFT ） ，通用机器学习原子间势（ MLIP ） ， MD和温度依赖性有效声子计算来研究单层1T-TaS2中CDW跃迁的结构和振动特征。针对DFT位移能量的基准测试可识别UMA-s-1p1通用机器学习电位，具有足够的准确性，可用于后续的有限温度模拟。 QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS 这些发现表明，经过仔细基准测试的通用MLIP可以为CDW材料的有限温度研究提供一个可扩展的框架。
**讨论重点：** 在这里，我们结合密度泛函理论（ DFT ） ，通用机器学习原子间势（ MLIP ） ， MD和温度依赖性有效声子计算来研究单层1T-TaS2中CDW跃迁的结构和振动特征。这些发现表明，经过仔细基准测试的通用MLIP可以为CDW材料的有限温度研究提供一个可扩展的框架。 结合关键词看，阅读时应重点关注机器学习分子动力学相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 8. A high-dimensional neural network potential for finite-temperature phenomena in NiTi martensite

- Source: arXiv
- Date: 2026-07-22T19:32:23Z
- Venue: cond-mat.mtrl-sci
- Authors: Petr Jaroš, Petr Sedlák, Petr Šesták, Miroslav Černý, Jörg Behler, Hanuš Seiner
- Link: https://arxiv.org/abs/2607.20681v1
- Score: 8.0
- Match: 标题匹配 neural network potential

**中文摘要：** 我们针对密度泛函理论（ DFT ）数据训练的NiTi形状记忆合金的马氏体相提出了一种高维神经网络势（ HDNNP ）。这项工作的一个核心方面是系统地验证了控制结构演化的关键属性的潜在DFT参考方法，包括平衡晶体结构、弹性常数、广义堆叠断层能量和振动光谱。 HDNNP准确描述了B19 $ ^\ prime $和B33相的相对稳定性，包括meV/原子量级的微小能量差异。预测的堆叠断层能量景观具有强烈的各向异性，揭示了优先剪切路径，提供了对变形和孪生机制的原子学见解。有限温度分子动力学模拟进一步支持对作为温度函数的无约束结构演化的研究。 总体而言，开发的HDNNP为在纳秒时间尺度上含有数十万个原子的马氏体NiTi系统的复杂结构和功能行为的原子学模拟提供了坚实的基础。
**讨论重点：** 我们针对密度泛函理论（ DFT ）数据训练的NiTi形状记忆合金的马氏体相提出了一种高维神经网络势（ HDNNP ）。这项工作的一个核心方面是系统地验证了控制结构演化的关键属性的潜在DFT参考方法，包括平衡晶体结构、弹性常数、广义堆叠断层能量和振动光谱。 结合关键词看，阅读时应重点关注神经网络势相关的模拟体系、时间尺度、温度条件、动力学稳定性，以及有限温度性质对势函数质量的敏感性。

### 9. Study of ordering in (MoCrTi)$_{100-x}$Al$_x$ refractory high-entropy alloys using machine learning interatomic potential

- Source: arXiv
- Date: 2026-07-20T16:01:06Z
- Venue: cond-mat.mtrl-sci, cond-mat.dis-nn
- Authors: Jiyao Zhang, Klemens Lechner, Markus Maßwohl, Petra Spoerk-Erdely, David Holec
- Link: https://arxiv.org/abs/2607.18099v2
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential

**中文摘要：** 难熔高熵合金是高温应用的有希望的候选材料，但成分对其化学有序途径和机械性能的影响仍未得到充分了解。在这里，采用通用MLIP结合MC和MD模拟来研究（ MoCrTi ） （ 100-x ） Alx合金的温度依赖性热力学和机械性能。 QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS 这种异常增强源于SRO诱导的原子对，特别是Mo-Cr对的重新分布。这些结果在合金成分、多级化学有序性和机械刚度之间建立了直接的原子学联系，为通过成分控制来调节RHEAs的机械行为提供了指导。
**讨论重点：** 在这里，采用通用MLIP结合MC和MD模拟来研究（ MoCrTi ） （ 100-x ） Alx合金的温度依赖性热力学和机械性能。原子构型、亚晶格占位和模拟衍射强度揭示了低温下明显的B2型化学有序性，其中Mo和Al占据一个亚晶格， Cr和Ti占据另一个亚晶格。 结合关键词看，阅读时应重点关注机器学习原子间势相关的自由能路径、相稳定性、热力学量的不确定性，以及势函数误差如何传递到宏观性质。

### 10. RuNNer 2.0: A Software Suite for High-Dimensional Neural Network Potentials

- Source: arXiv
- Date: 2026-07-20T14:13:35Z
- Venue: physics.chem-ph, cond-mat.mtrl-sci, physics.comp-ph
- Authors: Alexander L. M. Knoll, Moritz R. Schäfer, K. Nikolas Lausch, Moritz Gubler, Henry Wang, Richard Springborn
- Link: https://arxiv.org/abs/2607.17978v1
- Score: 8.0
- Match: 标题匹配 neural network potential

**中文摘要：** 我们提出了RuNNer 2.0 ，即“鲁尔大学神经网络能量表示” ，这是一个高度优化的软件套件，用于训练和评估第二代、第三代和第四代高维神经网络潜能（ HDNNP ）。 QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS 通过详细的基准测试证明了RuNNer 2.0生态系统的高效性和可扩展性。
**讨论重点：** 我们提出了RuNNer 2.0 ，即“鲁尔大学神经网络能量表示” ，这是一个高度优化的软件套件，用于训练和评估第二代、第三代和第四代高维神经网络潜能（ HDNNP ）。 第四代（ 4G ） HDNNP中非局部电荷转移描述的长程静电和电荷平衡（ QEq ）通过准线性缩放平面波方法加速，将QEq计算复杂度从$\ mathcal {O} (N ^ 3) $降低到$\ mathcal {O} (N\ log ^ 2 N) $ ，从而在所有HDNNP世代中实现线性或准线性缩放。 结合关键词看，阅读时应重点关注神经网络势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

## 凝聚态物理强关联体系和多铁性质

### 1. Efficient quantum implementation of dynamical mean field theory for correlated materials

- Source: Journal
- Date: 2026-08-17
- Venue: npj Computational Materials
- Authors: Norman Hogan, Efekan Kökcü, Thomas Steckmann, Liam P. Doak, Carlos Mejuto-Zaera, Daan Camps
- Link: https://doi.org/10.1038/s41524-026-02289-2
- Score: 9.0
- Match: 标题匹配 dynamical mean field theory; 近两周发布

**中文摘要：** 当前元数据未提供原文摘要。论文题目为“Efficient quantum implementation of dynamical mean field theory for correlated materials”。
**讨论重点：** 结合关键词看，阅读时应重点关注动力学平均场理论相关的研究对象、方法假设、关键参数、数据来源，以及结果能否迁移到相邻材料或物理体系。
