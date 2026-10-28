# Latest papers for 程旭丽

Updated: 2026-10-28T03:42:55.331780+00:00
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

**中文摘要：** QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS 我们进一步表明，钪掺杂促进$ V_\ mathrm {N} $的形成，从而增强缺陷介导的成核并减少$ E_\ mathrm {c} $。这些发现建立了管理薄膜畴生长动力学和宏观$ E_\ mathrm {c} $的多尺度机制，将实验观测与理想的晶体模拟相协调，并为低电压、可靠和可扩展的铁电器件提供缺陷工程原理。
**讨论重点：** 氮化铝基铁电体结合了高剩余极化、热稳定性、弱尺寸效应、宽带隙和后端工艺兼容性，使其有望实现高密度非易失性存储器。然而，它们的高矫顽场（ $ E_\ mathrm {c} $ ）和不清楚的极化切换机制限制了进一步的应用。 结合关键词看，阅读时应重点关注深度势分子动力学相关的极化翻转、磁电耦合、自旋-晶格耦合以及多铁序参量之间的相互制约。

### 2. Concentration-Dependent Speciation in ZnCl2 Electrolyte Solutions: Transferability of Machine-Learning Interatomic Potentials and Speciation Sensitivity of EXAFS

- Source: arXiv
- Date: 2026-10-21T22:46:57Z
- Venue: physics.chem-ph
- Authors: Junhan Chen, Luke D. Gibson, Nadia N. Intan, Darren M Driscoll, Mahalingam Balasubramanian, John L. Fulton
- Link: https://arxiv.org/abs/2610.30513v1
- Score: 11.0
- Match: 摘要匹配 DeepMD; 最近 3 天发布

**中文摘要：** QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS DFT治疗强烈影响协调自由能和聚集；排除与Zn相关的D3校正并不能系统地改善EXAFS一致性。CMD显示出更大的光谱差异和不一致的协调趋势。MACE-MATPES-r2SCAN改进了CMD ，产生了与DPMD-SCAN相当的光谱，提供了更一致的一致性和更高的计算效率。 邻域分辨分析表明，距离无序和散射路径干扰可以为不同的协调集合产生相似的EXAFS特征，这突出了严格采样和集合平均光谱以区分与氯桥接锌种类的必要性。
**讨论重点：** 我们将Zn K边缘扩展X射线吸收精细结构（ EXAFS ）测量与长时间尺度分子动力学（ MD ）相结合，使用机器学习原子间电位研究从稀释到30 m的ZnCl2水溶液。我们训练基于revPBE的DeepMD模型，包括或排除含锌对的D3校正，并将其与DPMD-SCAN、经典MD （ CMD ）和MACE-MATPES-r2SCAN进行比较。 结合关键词看，阅读时应重点关注DeepMD相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 3. Scalable long-range machine learning interatomic potentials with electrical response for atomistic material modeling

- Source: arXiv
- Date: 2026-10-16T15:44:07Z
- Venue: cond-mat.mtrl-sci, cs.LG
- Authors: Yicheng Chen, Xiaoyun Yu, Hyejeong Song, Xintian Wang, Zihui Li, Zixi Xia
- Link: https://arxiv.org/abs/2610.23643v1
- Score: 10.0
- Match: 标题匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS 在这里，我们通过将远程静电力和天然有效电荷（ BEC ）分析性地分离成全局静电计算和已知潜在电荷的严格局部导数来克服这一局限性。该配方保留了等变MLIP的空间可分解性，同时允许在不同边界条件下对能量、力、应力和BEC进行分布式评估。 该框架在\ texttt {nvalchemi}平台上实现为DPA4C-LR ，在四个GPU上扩展到520万个原子，其计算成本大约是其短程骨干网的两倍。经过能量和力的训练， DPA4C-LR准确地推断出BEC ，并再现了水的场相关红外光谱。 我们进一步展示了它的能力，恢复了松弛体\ ce {Pb (Mg_{1/3} Nb_{2/3}) O3}的特征极化迟滞，这种迟滞在较小的模拟中被有限尺寸效应所掩盖；预测了非晶态\ ce {Li_{0.9} NbO_{0.9} Cl_{4.1}}中的室温场驱动离子电导率为$ 6.8\ pm 0.7 $ ~ mS/cm ；并用平板校正的静电学对硅/金刚石界面上的界面热传输进行建模。
**讨论重点：** 严格的局部模型实现了高效的空间并行化，但忽略了远程相互作用，而现有的静电扩展引入了阻碍分布式计算的全局依赖性。该框架在\ texttt {nvalchemi}平台上实现为DPA4C-LR ，在四个GPU上扩展到520万个原子，其计算成本大约是其短程骨干网的两倍。 结合关键词看，阅读时应重点关注机器学习原子间势相关的第一性原理设置、对称性分析、能带或响应函数计算，以及这些量与可观测物性的对应关系。

### 4. Machine Learning-Assisted Discovery of Carbon-Related Defect Formation Mechanisms in Diamond

- Source: arXiv
- Date: 2026-10-19T12:51:02Z
- Venue: cond-mat.mtrl-sci
- Authors: Grace Huang, Christopher Fivecoat, Xun Xu, Mengen Wang
- Link: https://arxiv.org/abs/2610.26301v1
- Score: 9.0
- Match: 摘要匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS
**讨论重点：** 为了研究这种动力学驱动的过程并揭示中性电荷状态下二间隙和二空位的形成机制，我们使用密度泛函理论计算生成的小数据集微调了通用机器学习的原子间势。在通过辐照和随后的热退火产生缺陷的过程中，会产生与碳相关的缺陷，包括空位和间隙，并且可以迁移以形成新的缺陷复合体。 结合关键词看，阅读时应重点关注机器学习原子间势相关的第一性原理设置、对称性分析、能带或响应函数计算，以及这些量与可观测物性的对应关系。

### 5. From Algebraic Completeness to Orbit Separation: Recursive Separating Invariants for Global Neural Network Potential Energy Surfaces

- Source: arXiv
- Date: 2026-10-15T11:20:02Z
- Venue: physics.chem-ph
- Authors: Yiping Hao, Jing Lou, Bina Fu, Dong H. Zhang
- Link: https://arxiv.org/abs/2610.21700v1
- Score: 9.0
- Match: 标题匹配 neural network potential; 近两周发布

**中文摘要：** QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS 这些结果确立了轨道分离作为开发全局神经网络PES的高效对称保持描述符的一个有希望的原则。
**讨论重点：** 这里，我们引入递归分离不变量（ RSI ） ，将描述符设计原理从代数完备性转变为轨道分离。基本不变量（ FI ）形成了一个代数完整的生成集，大大减少了描述符的数量，并为更大的系统启用了神经网络PES。 结合关键词看，阅读时应重点关注神经网络势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 6. Instability-driven segregation of V group transition metals on HEB$_2$ grain boundaries influencing enhanced mechanical properties

- Source: arXiv
- Date: 2026-10-18T14:26:28Z
- Venue: cond-mat.mtrl-sci
- Authors: Daniil Alekseev, Viktor S. Baidyshev, Alexander G. Kvashnin
- Link: https://arxiv.org/abs/2610.25295v1
- Score: 8.0
- Match: 摘要匹配 MACE potential; 近两周发布

**中文摘要：** 五种金属在(Hf, Ta, Ti, Nb, Zr) B $_2 $ (HEB $_2 $)中共享一个共同的亚晶格。大多数高熵材料都是以烧结陶瓷的形式作为多晶材料生产的。哪些金属物种位于晶界的问题仍然未知。在这里，我们使用密度泛函理论（ DFT ）计算了五个二硼化物和HEB $_2 $中四种类型边界的晶界能$ γ_{GB} $。 我们使用COHP和HEB $_2 $六个边界的采样阳离子偏析分析了这些边界的键合，有序和一般，使用蒙特卡罗/分子动力学，具有针对该系统微调的MACE电位。根据我们的结果， $ γ_{GB} $按组分裂：组V二硼化物NbB $_2 $和TaB $_2 $在四种GB中的三种类型上形成边界，能量约为组IV的一半，范围为0.8至2.7 ，而2.5--4.8~J/m $ ^ 2 $。 QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS HEB $_2 $的晶界由V族金属组成，如二元化合物的边界能及其在费米能级上的键合所暗示的那样。(Hf, Ta, Ti, Nb, Zr) B $_2 $的晶界优先包括Nb和Ta。这降低了晶界能量并加强了边界。这包括下边界能量并改变NBB $_2 $和TaB $_2 $中的费米能级键。
**讨论重点：** 五种金属在(Hf, Ta, Ti, Nb, Zr) B $_2 $ (HEB $_2 $)中共享一个共同的亚晶格。大多数高熵材料都是以烧结陶瓷的形式作为多晶材料生产的。 结合关键词看，阅读时应重点关注MACE 势函数相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 7. Theoretical Investigation of Oxygen-Vacancy Diffusion in SrTiO$_3$ using Neural Network Potentials

- Source: arXiv
- Date: 2026-10-12T10:10:35Z
- Venue: cond-mat.mtrl-sci
- Authors: Kazutaka Nishiguchi, Ryota Yamamoto, Seiichiro Ten-no
- Link: https://arxiv.org/abs/2610.16521v1
- Score: 8.0
- Match: 标题匹配 neural network potential; 近两周发布

**中文摘要：** QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS 在这项研究中，我们使用AIMD模拟生成的参考数据集开发了原始和缺氧STO的神经网络电位（ NNP ）。训练的NNP模型准确地再现了含有氧空位的原始STO和STO的DFT参考能量、原子力和病毒。NNP还再现了总能量和氧空位形成能量的超级细胞大小依赖性，包括推断到稀释极限的形成能量。 然后使用NNP （ NNP-MD ）进行大规模和长期的MD模拟，以研究氧空位扩散。与传统的经典MD模拟相比，所得氧空位扩散系数与实验数据显示出更好的一致性。Arrhenius分析得出氧空位迁移焓为0.64 eV ，与0.67 eV的实验值非常一致。 这些结果表明，在第一原理数据上训练的NNP为研究钙钛矿氧化物中的缺陷形成和长期空位传输提供了准确且计算效率高的框架。
**讨论重点：** 在这项研究中，我们使用AIMD模拟生成的参考数据集开发了原始和缺氧STO的神经网络电位（ NNP ）。训练的NNP模型准确地再现了含有氧空位的原始STO和STO的DFT参考能量、原子力和病毒。 结合关键词看，阅读时应重点关注神经网络势相关的模拟体系、时间尺度、温度条件、动力学稳定性，以及有限温度性质对势函数质量的敏感性。

### 8. Long-Range Machine Learning Interatomic Potentials for Defect Energetics in SrTiO$_3$

- Source: arXiv
- Date: 2026-09-30T22:33:45Z
- Venue: cond-mat.mtrl-sci
- Authors: Yee Chit Wong, Marcel F. Langer, Reinhard J. Maurer, Nicholas D. M. Hine
- Link: https://arxiv.org/abs/2610.00794v1
- Score: 8.0
- Match: 标题匹配 machine learning interatomic potential

**中文摘要：** 近年来，机器学习的原子间电位（ MLIP ）发展迅速，但大多数模型本质上仍然是半局部的，忽略了远距离静电相互作用。为了解决这一局限性，已经出现了越来越多的远程模型，但比较它们在物理现实系统上的性能的系统基准仍然很少。 QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS 作为一个物理驱动的基准系统，我们专注于钛酸锶SrTiO $_3 $和Sr--O肖特基空位对，这是一种远程电荷相互作用发挥核心作用的材料，是研究带电极化子和其他电子和光学性质的天然垫脚石。 在此基准的基础上，我们进一步研究了在Sr-O肖特基对存在下的氧空位迁移，使用爬坡图像推动的弹性带计算和分子动力学来获得作为空位对分离函数的活化屏障，提供每个模型捕获控制缺陷输运的静电效应的能力的进一步外推测试。
**讨论重点：** QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 9. Reticulating Local Dynamics in Three-Dimensional Covalent Organic Frameworks

- Source: arXiv
- Date: 2026-10-17T03:30:37Z
- Venue: cond-mat.mtrl-sci
- Authors: Francesco Tavani, Saber Mirzaei, M. Saeed Mirzaei, Jian Yin, Yen-hsu Lin, Caden Myers
- Link: https://arxiv.org/abs/2610.24418v1
- Score: 7.0
- Match: 摘要匹配 machine learning interatomic potential; 近两周发布

**中文摘要：** 在共价有机框架（ COF ）中，建筑单元的几何形状预先确定了框架的结构，但将COF连接子与控制客体吸附和扩散的局部运动以及机械响应相关的可比设计原则仍然遥不可及。（部分摘要片段自动翻译失败，建议打开原文核对完整摘要。）
**讨论重点：** 可重点阅读摘要中关于研究对象、方法设计和关键验证的描述。 结合关键词看，阅读时应重点关注机器学习原子间势相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

### 10. Benchmarking machine-learning interatomic potentials using classical force fields

- Source: arXiv
- Date: 2026-10-09T18:56:31Z
- Venue: cond-mat.mtrl-sci
- Authors: Johannes Sandberg, Geneviève Dusson, Julien Lam
- Link: https://arxiv.org/abs/2610.14239v1
- Score: 7.0
- Match: 摘要匹配 neural network potential; 摘要匹配 MACE potential

**中文摘要：** 自动翻译暂不可用，以下为原文摘要：We propose a rational comparison between several well-known machine-learning interatomic potentials (linear atomic cluster expansion, the Behler-Parrinello high-dimensional neural network potential, and the graph neural network-based MACE potential) by testing their performance for fitting classical potentials such as the Lennard-Jones and Stillinger-Weber potential. With this we assess their advantages and limitations regarding several aspects: varying training dataset size, robustness to noise, carbon footprint, as well as the ability to reproduce the radial distribution function as an example observable. Overall the MACE models are shown to most accurately reproduce the potential energy surface, with little sign of overfitting, but at a significant computational cost, highlighting important questions regarding the choice of models in computational materials science.
**讨论重点：** 可重点阅读摘要中关于研究对象、方法设计和关键验证的描述。 结合关键词看，阅读时应重点关注神经网络势、MACE 势函数相关的基准数据集、评价指标、误差来源，以及不同模型在精度、效率和可迁移性之间的取舍。

## 凝聚态物理强关联体系和多铁性质

### 1. Finite-width altermagnetic quantum rings: angular-channel hybridization and Aharonov--Bohm physics

- Source: arXiv
- Date: 2026-10-21T23:43:38Z
- Venue: cond-mat.mes-hall, quant-ph
- Authors: Edilberto O. Silva
- Link: https://arxiv.org/abs/2610.30536v1
- Score: 22.0
- Match: 标题匹配 altermagnetic; 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS（部分摘要片段自动翻译失败，建议打开原文核对完整摘要。）
**讨论重点：** 可重点阅读摘要中关于研究对象、方法设计和关键验证的描述。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 2. Emergent altermagnetism in (LaVO$_3$)$_n$/(LaNiO$_3$)$_m$ superlattices from interfacial charge transfer and octahedral tilts

- Source: arXiv
- Date: 2026-10-21T19:31:42Z
- Venue: cond-mat.str-el, cond-mat.mtrl-sci
- Authors: Gustavo H. Cassemiro, Walber H. Brito
- Link: https://arxiv.org/abs/2610.30371v1
- Score: 22.0
- Match: 标题匹配 altermagnetism; 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** 自动翻译暂不可用，以下为原文摘要：Using first-principles calculations, we show that altermagnetism emerges in (LaVO$_3$)$_n$/(LaNiO$_3$)$_m$ superlattices, with $(n,m) = (1,1), (2,2)$ and $(2,4)$, from the interplay of interfacial charge transfer and octahedral tilts. Charge transfer drives the system towards the V$^{4+}$ and Ni$^{2+}$ configuration, turning the otherwise paramagnetic nickelate layers into a magnetically active sublattice. The resulting $C$-type antiferromagnetic order, combined with $a^-b^+c^-$ or $a^-b^-c^-$ octahedral tilts, links opposite-spin sublattices only through nonsymmorphic operations, yielding a $d$-wave spin splitting without spin-orbit coupling. Within DFT+U, the splitting reaches 118 meV in the insulating (LVO)$_1$/(LNO)$_1$ superlattice, about twice that calculated for bulk LaVO$_3$, and decreases as the nickelate layers become thicker. Our findings indicate that this splitting is hosted by both the V and Ni sublattices, with nearly half of its weight on oxygen $2p$ states through $p$-$d$ covalency. Interfacial charge transfer thus emerges as a \textit{design} principle for engineering altermagnetism in oxide heterostructures.
**讨论重点：** 可重点阅读摘要中关于研究对象、方法设计和关键验证的描述。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 3. Extreme competition between stripes and superconductivity in the hole-doped Hubbard model

- Source: arXiv
- Date: 2026-10-21T18:33:57Z
- Venue: cond-mat.str-el, cond-mat.dis-nn, cond-mat.supr-con
- Authors: Ao Chen, Johnnie Gray, Si-Jing Du, Garnet Kin-Lic Chan
- Link: https://arxiv.org/abs/2610.30321v1
- Score: 18.0
- Match: 标题匹配 Hubbard model; 摘要匹配 tensor network; 最近 3 天发布

**中文摘要：** 自动翻译暂不可用，以下为原文摘要：The two-dimensional Hubbard model was originally proposed as the minimal model of uniform $d$-wave superconductivity in the cuprate high-temperature superconductors, but recent calculations with relevant parameters in a realistic doping regime have often found other ground states. Further, uncertainty remains over such results due to the intrinsic bias of different computational methods. Here we address this uncertainty through state-of-the-art neural tensor network and neural backflow state simulations, enabled by large-scale GPU computation, that together reach an unprecedented variational accuracy on lattices with up to 1024 sites. At $1/8$ doping in the pure Hubbard model, as well as with next-nearest-neighbor hopping relevant to the hole-doped cuprates, we reveal a near degeneracy among a low-energy uniform $d$-wave state, superconducting stripes, and non-superconducting stripe states on the milli-$t$ energy scale. Our work rebalances the narrative that the Hubbard model supports a single dominant order in relevant parameter regimes towards a picture of extreme competition between stripes and superconductivity.
**讨论重点：** 可重点阅读摘要中关于研究对象、方法设计和关键验证的描述。 结合关键词看，阅读时应重点关注Hubbard 模型、张量网络相关的有效模型参数、电子关联强度、相图边界以及可与实验对照的谱学或输运信号。

### 4. $π$-Flux Tuning of Quantum Paramagnetism in the Triangular-Lattice Hubbard Model

- Source: arXiv
- Date: 2026-10-21T18:07:15Z
- Venue: cond-mat.str-el
- Authors: Zhaochen Liu, Andreas Feuerpfeil, Ronny Thomale
- Link: https://arxiv.org/abs/2610.30290v1
- Score: 18.0
- Match: 标题匹配 Hubbard model; 摘要匹配 density matrix renormalization group; 最近 3 天发布

**中文摘要：** 自动翻译暂不可用，以下为原文摘要：We compare two time-reversal-symmetric triangular-lattice Hubbard models at half filling: the zero-flux model and a staggered $π$-flux model with zero and $π$ flux through oppositely oriented triangles. Although both reduce to the same Heisenberg model at leading order in the strong-coupling limit, their distinct charge fluctuation profiles yield different quantum paramagnetic regimes. Combining a strong-coupling expansion with infinite density matrix renormalization group (iDMRG) calculations, we find that the positive ring-exchange of the zero-flux model promotes spontaneous chirality, consistent with its notion of a chiral spin liquid at intermediate coupling. In the staggered-$π$-flux model, whose noninteracting limit is a Dirac semimetal, the ring exchange changes sign and disfavors chiral order and we find no resolvable scalar chirality. This renders flux-tuned ring-exchange an efficient discriminator between chiral and non-chiral quantum paramagnets at finite coupling.
**讨论重点：** 可重点阅读摘要中关于研究对象、方法设计和关键验证的描述。 结合关键词看，阅读时应重点关注Hubbard 模型、密度矩阵重整化群相关的有效模型参数、电子关联强度、相图边界以及可与实验对照的谱学或输运信号。

### 5. Microscopic origin of field-induced multiferroicity in Ni3TeO6

- Source: arXiv
- Date: 2026-10-21T08:45:40Z
- Venue: cond-mat.mtrl-sci
- Authors: J. Lass, R. Toft-Petersen, A. A. Turrini, Ø. S. Fjellvåg, B. Decrausaz, K. M. L. Krighaar
- Link: https://arxiv.org/abs/2610.29420v1
- Score: 18.0
- Match: 标题匹配 multiferroic; 摘要匹配 multiferroic materials; 最近 3 天发布

**中文摘要：** QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS（部分摘要片段自动翻译失败，建议打开原文核对完整摘要。）
**讨论重点：** 可重点阅读摘要中关于研究对象、方法设计和关键验证的描述。 结合关键词看，阅读时应重点关注多铁性、多铁材料相关的极化翻转、磁电耦合、自旋-晶格耦合以及多铁序参量之间的相互制约。

### 6. Piezo-Kerr effect in altermagnets and noncollinear antiferromagnets

- Source: arXiv
- Date: 2026-10-22T08:49:03Z
- Venue: cond-mat.mtrl-sci, cond-mat.mes-hall
- Authors: Yuqi Liu, Qiu-Shi Huang, Xinfeng Chen, Yilin Han, Run-Wu Zhang, Zhi-Ming Yu
- Link: https://arxiv.org/abs/2610.30929v1
- Score: 16.0
- Match: 标题匹配 altermagnet; 最近 3 天发布

**中文摘要：** QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS
**讨论重点：** 可重点阅读摘要中关于研究对象、方法设计和关键验证的描述。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 7. Sign-problem-free Bosonic Auxiliary Field Quantum Monte Carlo

- Source: arXiv
- Date: 2026-10-22T16:48:36Z
- Venue: cond-mat.str-el, cond-mat.quant-gas, cond-mat.stat-mech
- Authors: Yin-Kai Yu, Zhong-Chao Wei, Zi-Xiang Li
- Link: https://arxiv.org/abs/2610.31541v1
- Score: 15.0
- Match: 摘要匹配 Hubbard model; 摘要匹配 quantum many-body; 最近 3 天发布

**中文摘要：** QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS
**讨论重点：** 可重点阅读摘要中关于研究对象、方法设计和关键验证的描述。 结合关键词看，阅读时应重点关注Hubbard 模型、量子多体相关的有效模型参数、电子关联强度、相图边界以及可与实验对照的谱学或输运信号。

### 8. Ferroelastic Reversal Magnon Thermal Hall Effect in a Fully Compensated Ferrimagnet

- Source: arXiv
- Date: 2026-10-22T05:01:12Z
- Venue: cond-mat.mes-hall
- Authors: Yingxi Bai, Zihan Chen, Chengwang Niu, Ming Yang
- Link: https://arxiv.org/abs/2610.30733v1
- Score: 15.0
- Match: 摘要匹配 altermagnetic; 摘要匹配 altermagnet; 最近 3 天发布

**中文摘要：** QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS（部分摘要片段自动翻译失败，建议打开原文核对完整摘要。）
**讨论重点：** 可重点阅读摘要中关于研究对象、方法设计和关键验证的描述。 结合关键词看，阅读时应重点关注交变磁性相关的交变磁性的对称性来源、动量空间自旋劈裂，以及这些特征如何影响输运、光学或磁动力学响应。

### 9. Unrestricted Binary Tree State for the Fermionic Hubbard Model

- Source: arXiv
- Date: 2026-10-21T20:04:02Z
- Venue: cond-mat.str-el
- Authors: Mahroo Mirabdolhagh Hazaveh, Armin Khamoshi, Fei Gao, Thomas M. Henderson, Gustavo E. Scuseria
- Link: https://arxiv.org/abs/2610.30399v1
- Score: 15.0
- Match: 标题匹配 Hubbard model; 最近 3 天发布

**中文摘要：** QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS（部分摘要片段自动翻译失败，建议打开原文核对完整摘要。）
**讨论重点：** 可重点阅读摘要中关于研究对象、方法设计和关键验证的描述。 结合关键词看，阅读时应重点关注Hubbard 模型相关的有效模型参数、电子关联强度、相图边界以及可与实验对照的谱学或输运信号。

### 10. Projective symmetry groups beyond spin-$1/2$: Classifying integer-spin quantum spin liquids

- Source: arXiv
- Date: 2026-10-21T17:08:50Z
- Venue: cond-mat.str-el
- Authors: Atanu Maity, Chunxiao Liu, Rhine Samajdar, Yasir Iqbal
- Link: https://arxiv.org/abs/2610.30048v1
- Score: 15.0
- Match: 标题匹配 quantum spin liquid; 最近 3 天发布

**中文摘要：** QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS QUERY LENGTH LIMIT EXCEEDED. MAX ALLOWED QUERY : 500 CHARS（部分摘要片段自动翻译失败，建议打开原文核对完整摘要。）
**讨论重点：** 可重点阅读摘要中关于研究对象、方法设计和关键验证的描述。 结合关键词看，阅读时应重点关注量子自旋液体相关的新方法的假设、训练或计算流程、适用体系，以及与已有方法相比的优势和局限。
